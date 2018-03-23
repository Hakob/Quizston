from time import sleep

from django.shortcuts import render
from django.views import View
from .models import PossibleAnswers, Answers, Questions
from random import randint, shuffle
import csv
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm


class MyView(View):
    answered_q_id = [0]
    template_name = 'start.html'
    quality = {'points': 0,
               'inc': 5,
               'delta': 3}

    def get(self, request):
        if 'X-CSRFToken' in request.META:
            answer = request.GET.get('answer')
            data = {
                'is_true': False
            }
            if answer == self.answered_q_id[-1]:
                self.quality['points'] += self.quality['inc']
                self.quality['inc'] += self.quality['delta']
                data['is_true'] = True
                data['true_answer'] = self.answered_q_id[-1]
            self.answered_q_id.pop()

            return JsonResponse(data)
        else:
            if self.answered_q_id[0]:
                self.answered_q_id[:] = [0]
            return render(request, 'start.html', context=None)

    def post(self, request):
        if len(self.answered_q_id) - 1 == 5:
            context = {'points': self.quality['points']}
            response = render(request, 'home.html', context=context)
            self.answered_q_id = [0]
            self.quality['points'] = 0
            self.quality['inc'] = 5
            return response

        random_q_id = randint(1, 18)
        while random_q_id in self.answered_q_id:
            random_q_id = randint(1, 18)
        self.answered_q_id.append(random_q_id)

        question = Questions.objects.get(auto_increment_id=random_q_id)
        true_answer = Answers.objects.get(which_questions_answer__auto_increment_id=random_q_id)
        possible_answers = PossibleAnswers.objects.get(questions_possible_answers__auto_increment_id=random_q_id)
        pos_ans = list(csv.reader(str(possible_answers).splitlines(), delimiter=','))[0]
        true_answer = str(true_answer)
        self.answered_q_id.append(true_answer)
        pos_ans.append(true_answer)
        shuffle(pos_ans)
        context = {
            'question': str(question),
            'possible_answers': pos_ans,
        }

        response = render(request, self.template_name, context=context)
        return response
