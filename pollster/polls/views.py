from django.shortcuts import render
from .models import pollQuestion,Choice

# Create your views here.


def index(request):
  poll_question_list = pollQuestion.objects.all()
  context = {"poll_question_list":poll_question_list}
  return render(request,'polls/index.html',context)


def details(request,questionid):
  try:
    question=pollQuestion.objects.get(pk=questionid)
  except pollQuestion.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request,'polls/detail.html',{"question":question})


def results(request,questionid):
  question = get_object_or_404(pollQuestion,pk=questionid)
  return render(request,'polls/results.html',{"question":question})








