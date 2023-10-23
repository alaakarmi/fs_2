from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("add/", views.RequestCreateView.as_view(), name="add"),
    path("update/<int:pk>", views.RequestUpdateView.as_view(), name="update"),
]