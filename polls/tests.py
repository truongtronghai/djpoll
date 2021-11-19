import datetime
from django.utils import timezone
from django.test import TestCase  # using for test
from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    # test method must begin with word "test"
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)  # time in future for test
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
