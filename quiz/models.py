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

