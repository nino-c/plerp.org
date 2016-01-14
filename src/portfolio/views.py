from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def mainindex(request):
	categories = models.PortfolioCategory.objects.all()
	return render(request, "home2.html", {'categories': categories})

def index(request):
	categories = models.PortfolioCategory.objects.all()
	return render(request, "portfolio/index.html", {'categories': categories})

def list_category(request, name):
	try:
		category = models.PortfolioCategory.objects.get(name__exact=name)
	except models.PortfolioCategory.DoesNotExist:
		return redirect('portfolio:index')

	if category.name == 'Proprietary':
		items = models.ProprietaryPortfolioItem.objects.filter(category__id=category.id)
	else:
		items = models.PortfolioItem.objects.filter(category__id=category.id)
	return render(request, "portfolio/list_category.html", {'category': category, 'items': items})

def show_item(request, id):
	return HttpResponse("plerp")