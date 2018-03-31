import csv
import json
from random import randint, shuffle

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import PossibleAnswers, Answers, Questions


class MyView(View):
    template_name = ''

    def put(self, request):
        if 'HTTP_X_CSRFTOKEN' in request.META:
            answer = json.loads(request.body.decode('utf-8'))
            data = {
                'is_true': False
            }
            if answer['answer'] == request.session['true_answer']:
                request.session['points'] += request.session['inc']
                request.session['inc'] += request.session['delta']
                data['is_true'] = True
            if not data['is_true']:
                data['true_answer'] = request.session['true_answer']

            return JsonResponse(data)

    def get(self, request):
        if not request.user.is_authenticated:
            request.session['points'] = 0
            request.session['inc'] = 5
            request.session['delta'] = 3
            request.session['answered_q_id'] = []
            return render(request, 'redirect.html')
        return JsonResponse({})

    def post(self, request):
        try:
            if len(request.session['answered_q_id']) == 5:
                context = {'points': request.session['points']}
                response = render(request, 'home.html', context=context)
                del request.session['answered_q_id']
                return response
        except KeyError:
            request.session['points'] = 0
            request.session['answered_q_id'] = []
            request.session['inc'] = 5
            request.session['delta'] = 3

        random_q_id = randint(1, 18)
        while random_q_id in request.session['answered_q_id']:
            random_q_id = randint(1, 18)

        request.session['answered_q_id'].append(random_q_id)

        question = Questions.objects.get(auto_increment_id=random_q_id)
        true_answer = Answers.objects.get(which_questions_answer__auto_increment_id=random_q_id)
        possible_answers = PossibleAnswers.objects.get(questions_possible_answers__auto_increment_id=random_q_id)
        stringed = str(possible_answers).splitlines()
        pos_ans = list(csv.reader(stringed, delimiter=','))[0]
        true_answer = str(true_answer)
        request.session['true_answer'] = true_answer
        pos_ans.append(true_answer)
        shuffle(pos_ans)
        context = {
            'question': str(question),
            'possible_answers': pos_ans,
        }
        response = render(request, self.template_name, context=context)
        return response
