from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question, Person
from django.views import generic
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('city') and request.POST.get('company'):
            post = Post()
            post.city = request.POST.get('city')
            post.company = request.POST.get('company')
            post.save()

            return render(request, 'posts/createpost.html')  

        else:
            return render(request,'posts/createpost.html')



class IndexView(generic.ListView):
    template_name = 'polls/createpost.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


