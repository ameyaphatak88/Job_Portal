from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from django.http import HttpResponseRedirect

def index(request):
    template = loader.get_template('portal/index.html')
    context = {
        'name':'Ameya',
    }
    return HttpResponse(template.render(context,request))


def simpleform(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'portal/simpleform.html', {'form': form})


def thanks(request):
    template = loader.get_template('portal/thanks.html')
    return HttpResponse(template.render({}, request))
