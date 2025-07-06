from django.test import TestCase
import datetime

from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recenttyl() must not return true for question with pub_date in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.asserIs(future_question.was_published_recently(), False)
# Create your tests here.
