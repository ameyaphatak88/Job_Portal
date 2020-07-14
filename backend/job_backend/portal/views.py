from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from django.http import HttpResponseRedirect
from .models import Job

def index(request):
    template = loader.get_template('portal/index.html')
    context = {
        'name':'Ameya',
    }
    return HttpResponse(template.render(context,request))


def simpleform(request):
    if request.method == 'POST':
        print("inside post")
        form = NameForm(request.POST)
        if form.is_valid():
            print("entering inside form-is-valid")
            company = form.cleaned_data['company']
            c = Job(company= company)
            c.save()
            return HttpResponseRedirect('thanks/')
        else:
            print("entering into else block")
    else:
        print("inside get")
        form = NameForm()
    return render(request, 'portal/simpleform.html', {'form': form})


def thanks(request):
    template = loader.get_template('portal/thanks.html')
    return HttpResponse(template.render({}, request))


def jobs_display(request):
    from portal.models import Job
    jobs = Job.objects.all()
    ljobs = list(jobs)
    fruit = ["apple", "banana", "cherry"]
    context = {'a':fruit}

    template = loader.get_template('portal/post_job.html')  
    return HttpResponse(template.render(context, request))


class Resultview: