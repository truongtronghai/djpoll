from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from .models import Question

# Create your views here.
# Each view is represented by a Python function or method


def index(request):
    # get 5 latest things
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # by convention, Dj searches template in dir /polls/templates/
    template = loader.get_template('polls/index.html')

    # preparing data for transfering to template
    context = {
        'five_latest_question_list': latest_question_list
    }

    return HttpResponse(template.render(context, request))
    # or shortcut of render() like this:
    # return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        '''
         question will consist of all choices related it
         Django will automatically join them because of relation in DB
         '''
        question = Question.objects.get(pk=question_id)  # pk => primary key
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    # or shortcut style of get and raise error:
    # question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'q': question})


def results(req, question_id):
    return HttpResponse("You are looking at the results of question: %s" % question_id)


def vote(req, question_id):
    return HttpResponse("You are voting on question: %s" % question_id)
