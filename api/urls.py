from django.urls import path
from django.http import HttpResponse, JsonResponse, Http404 

from.import views

urlpatterns = [
    path('', views.index, name='index'),


]