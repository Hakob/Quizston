from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Exam


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
def add_exam(request):
    if request.method == 'POST':
        exam_name = request.POST.get("exam_name")
        user = request.POST.get("user")
        exam = Exam()
        exam.name = exam_name
        exam.user = User.objects.get(pk=user)
        exam.save()
        return HttpResponse(exam.id)
