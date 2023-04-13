from django.http import HttpResponseForbidden
from django.shortcuts import render, HttpResponse, redirect


from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import PPL, Region
from .forms import PPLForms, RegisterForm, LoginAuthenticatedForm

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


class DeleteSummary(DeleteView):
    model = PPL
    success_url = reverse_lazy('home')


class Search(ListView):
    template_name = 'layout/home.html' # Ссылка на HTML файл
    context_object_name = 'ppl_db' # Делает переменную с объектом ppl_db
    paginate_by = 5 # Максимальное количество записей

    def get_queryset(self):
        print(self.request.GET)
        return PPL.objects.filter(profession__icontains=self.request.GET.get('search', ''))

    def get_context_data(self, *args, object_list = None, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['p'] = self.request.GET.get('p')
        return context

class ChangeSummary(UpdateView):
    template_name = 'layout/change.html'
    form_class = PPLForms
    model = PPL
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ppl_db'] = PPL.objects.all()
        return context

class Profile(View):
    def get(self, request):
        template = 'layout/profile.html'
        context = {'ppl_db' : PPL.objects.all()}
        return render(request, template, context)

class RegisterUser(CreateView):
    template_name = 'layout/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['ppl_db'] = PPL.objects.all()
        return context

class AuthenticationUser(LoginView):
    form_class = LoginAuthenticatedForm
    template_name = 'layout/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')
