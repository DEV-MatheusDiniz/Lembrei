from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from .models import Lembrete
from .forms import FormLembrete


#HOME
@login_required(login_url="/login/")
def index(request):
    lembretes = Lembrete.objects.filter(id_user=request.user)
    context = {'segment': 'index', 'lembretes': lembretes, 'i': 1}
    html_template = loader.get_template('index/index.html')
    return HttpResponse(html_template.render(context, request))

#ADICIONAR LEMBRETES
@login_required(login_url="/login/")
def addLembrete(request):
    form = FormLembrete(request.POST or None)
    context = {'segment': 'index', 'form': form}
    if form.is_valid():
        form = form.save(commit=False)
        form.id_user = request.user
        form.save()
        return redirect('lembretes')
    html_template = loader.get_template('index/addLembrete.html')
    return HttpResponse(html_template.render(context, request))

#ALTERAR LEMBRETES
@login_required(login_url="/login/")
def altLembrete(request, id):
    lembrete = Lembrete.objects.get(id=id)
    form = FormLembrete(request.POST or None, instance=lembrete)
    context = {'segment': 'index', 'form': form}
    if form.is_valid():
        form.save()
        return redirect('lembretes')
    html_template = loader.get_template('index/altLembrete.html')
    return HttpResponse(html_template.render(context, request))

#DELETAR LEMBRETES
@login_required(login_url="/login/")
def delLembrete(request, id):
    lembrete = Lembrete.objects.get(id=id)
    context = {'segment': 'index', 'lembrete': lembrete}
    if request.method == 'POST':
        lembrete.delete()
        return redirect('lembretes')
    html_template = loader.get_template('index/delLembrete.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
