from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse
from .models import Choice, Question
# Create your views here.

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     print(question)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {'question': question})
    # return HttpResponse("You are looking at Question: {}".format(question_id))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
    # return HttpResponse("You are looking at results for Question: %s" % question_id)

def vote(request, question_id):
    choice = request.POST["choice"]
    selected_question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = selected_question.choice_set.get(pk=choice)
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": selected_question,
            "error_message": "You did not select a choice"
        })
    else:
        print(selected_choice)
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(selected_question.id,)))
    # return HttpResponse("You are looking at votes for Question: %s" % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-published_date")[:5]
    template = loader.get_template("polls/index.html")
    # output = " ,".join([q.question_text for q in latest_question_list ])
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))
