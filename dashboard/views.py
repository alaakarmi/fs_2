from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from main.models import Request
from .filters import RequestFilter


class IndexView(LoginRequiredMixin, ListView):
    queryset = Request.objects.all()
    template_name = "dashboard/index.html"
    context_object_name = 'reqsts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RequestFilter(self.request.GET, queryset=queryset) 
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

