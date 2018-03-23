from django.db import models


class Questions(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.content


class Answers(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, blank=False)
    which_questions_answer = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class PossibleAnswers(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, blank=False)
    questions_possible_answers = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
