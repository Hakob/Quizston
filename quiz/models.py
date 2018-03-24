from django.contrib.auth.models import User
from django.db import models

# class UserDetail(models.Model):
#     name = models.CharField(max_length=50,default="")
#     email = models.CharField(max_length=50,default="")
#     password = models.CharField(max_length=50,default="")
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return self.name


class Exam(models.Model):
    name = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(max_length=200, blank=False)
    option1 = models.CharField(max_length=50, blank=False)
    option2 = models.CharField(max_length=50, blank=False)
    option3 = models.CharField(max_length=50, blank=False)
    option4 = models.CharField(max_length=50, blank=False)
    answer = models.CharField(max_length=50, blank=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
