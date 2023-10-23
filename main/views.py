from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from main.models import Request
from .forms import AddRequestForm, UpdateRequestForm

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "main/home.html"

    def get_context_data(self,*args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['reqsts'] = Request.objects.all().order_by('-date_added')
        return context


class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    form_class = AddRequestForm
    template_name = 'main/create.html'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = Request
    form_class = UpdateRequestForm
    template_name = "main/update.html"
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)