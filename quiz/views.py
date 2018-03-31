from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import BestResult


def validate_username(request):
    username = request.GET.get('Username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


# welcome screen
def welcome(request):
    if request.user.is_authenticated:
        return render(request, "exam.html")
    return render(request, "outdex.html")


@login_required
def get_data(request):
    return render(request, "exam.html")


# view for creating user
def create_user(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create_user(name, email, password)
    return render(request, "outdex.html")


# view for logging in
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("success")
            else:
                return HttpResponse("disabled account")
        else:
            return HttpResponse("invalid credentials")


@login_required
def log_out(request):
    logout(request)
    return render(request, "outdex.html")


@login_required
def update_result(request):
    if request.method == 'POST':
        user_id = int(request.POST.get("user_id"))
        points = int(request.POST.get("points"))
        try:
            old_result = BestResult.objects.get(user=user_id)
            if points > old_result.score:
                old_result.score = points
                old_result.save()
                return HttpResponse(status=202)

        except BestResult.DoesNotExist:
            result = BestResult(score=points, user=user_id)
            result.save()
            return HttpResponse(status=201)


@login_required
def top10(request):
    tops = BestResult.objects.order_by('-score')[:10]
    users = []
    scores = []
    tpl = ['name', 'score']
    for top in tops:
        users.append(str(top.user))
        scores.append(top.score)
    scores = list(zip(users, scores))
    users[:] = []
    for i in scores:
        users.append(dict(zip(tpl, i)))
    context = {
        'users': users
    }
    return render(request, 'results.html', context=context)
