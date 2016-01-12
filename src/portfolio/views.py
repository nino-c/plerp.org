from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
	categories = models.PortfolioCategory.objects.all()
	return render(request, "portfolio/index.html", {'categories': categories})

def list_category(request, name):
	return HttpResponse('plerp')