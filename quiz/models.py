from django.contrib.auth.models import User
from django.db import models


class BestResult(models.Model):
    score = models.PositiveSmallIntegerField(help_text="Integer score in a range from 0 through 32767")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
