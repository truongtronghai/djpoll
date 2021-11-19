from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Question, Choice

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
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(req, 'polls/results.html', {'question': q})


def vote(req, question_id):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    try:
        selected_choice = q.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(req, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))
