from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

def home_window(request):
    ppl_db = PPL.objects.all()
    template = 'layout/home.html'
    context = {'ppl_db' : ppl_db}
    return render(request, template, context)

class CreatePPLView(CreateView):
    template_name = 'layout/add.html'
    model = PPL
    form_class = PPLForms
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ppl_db'] = PPL.objects.all()
        return context

def rubrics(request):
    if request.user.has_perms(('layout.add', ))
    else:
        return HttpResponseForbidden('Вы не имеете допуска к списку рубрик')
