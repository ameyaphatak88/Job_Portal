from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from django.http import HttpResponseRedirect
from .models import Job
from django.urls import reverse
from django.views import generic

def index(request):
    template = loader.get_template('portal/index.html')
    context = {
        'name':'Ameya',
    }
    return HttpResponse(template.render(context,request))


def simpleform(request):
    from portal.models import Job
    jobs = Job.objects.all()
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            city = form.cleaned_data['city']
            primary_skill = form.cleaned_data['primary_skill']
            min_work_experience = form.cleaned_data['min_work_experience']
            c = Job(company= company, city = city, primary_skill = primary_skill, min_work_experience = min_work_experience)
            
            flag = 0
            for ajob in jobs:
                if c.company.lower() == ajob.company.lower():
                    flag = 1
            if flag == 1:
                return HttpResponse("Cannot add as the company aldeady exists")
            
            c.save()
            return HttpResponseRedirect('jobs/')
    else:
        form = NameForm()
    return render(request, 'portal/simpleform.html', {'form': form})


def thanks(request):
    template = loader.get_template('portal/thanks.html')
    return HttpResponse(template.render({}, request))


def jobs_display(request):
    from portal.models import Job
    jobs = Job.objects.all()

    context = {
        "a":jobs
    }
    template = loader.get_template('portal/post_job.html')  
    return HttpResponse(template.render(context, request))

