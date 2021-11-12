from django.db import models

# Create your models here.


class Question(models.Model):  # each class  will be a Table in DB
    question_text = models.CharField(max_length=200)  # property is a column
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # override parent's method to return human-readable str
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
