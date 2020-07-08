from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question
from django.views import generic
from django.utils import timezone

def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(request))
    


class IndexView(generic.ListView):
    template_name = 'polls/index.html'




