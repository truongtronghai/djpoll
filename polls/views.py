# from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
# Each view is represented by a Python function or method


def index(request):
    latest_question_list = Question.objects.order_by(
        '-pub_date')[:5]  # get 5 latest things
    output_results = "<br> ".join(
        q.question_text for q in latest_question_list)
    return HttpResponse("<html><body><h1>Questions:</h1>%s</body></html>" % output_results)


def detail(request, question_id):
    return HttpResponse("<html><body><h1>You are looking at detail of question: %s</h1></body></html>" % question_id)


def results(req, question_id):
    return HttpResponse("You are looking at the results of question: %s" % question_id)


def vote(req, question_id):
    return HttpResponse("You are voting on question: %s" % question_id)
