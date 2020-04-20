from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404 

from django.utils import timezone

# Create your views here.

def index(request):
	context = {'data': 'pranav'}
	return  JsonResponse(context)