import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):  # each class  will be a Table in DB
    question_text = models.CharField(max_length=200)  # property is a column
    pub_date = models.DateTimeField('date published')
    # Python will automatically create

    def __str__(self):  # override parent's method to return human-readable str
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
