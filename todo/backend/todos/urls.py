
from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.DetailTodo.as_view(), name ='detail'),
    path('', views.ListTodo.as_view(), name ='index')
]