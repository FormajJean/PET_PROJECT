from django.http import HttpResponseForbidden
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.edit import CreateView
from django.views import View
from django.views.generic.list import ListView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.


import asyncio
from django.http import HttpResponse
from django.views import View


class Home_window(View):
    def get(self, request):
        ppl_db = PPL.objects.all()
        template = 'layout/home.html'
        context = {'ppl_db': ppl_db}
        return render(request, template, context)


def add(request):
    if request.method == 'POST':
        form = PPLForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print('fd')
    else:
        form = PPLForms
    context = {'form' : form}
    return render(request, 'layout/add.html', context)

def for_employees(request):
    ppl_db = PPL.objects.all()
    template = 'layout/for_employees.html'
    context = {'ppl_db': ppl_db}
    return render(request, template, context)

def for_employers(request):
    ppl_db = PPL.objects.all()
    template = 'layout/for_employers.html'
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


class Search(ListView):
    template_name = 'layout/home.html'
    context_object_name = 'ppl_db'
    paginate_by = 5
    def get_queryset(self):
        print(self.request.GET)
        return PPL.objects.filter(profession__icontains=self.request.GET.get('search', ''))

    def get_context_data(self, *args, object_list = None, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['p'] = self.request.GET.get('p')
        return context