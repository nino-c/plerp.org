from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def mainindex(request):
	categories = models.PortfolioCategory.objects.all()
	return render(request, "index.html", {'categories': categories})

# def index(request):
# 	categories = models.PortfolioCategory.objects.all()
# 	return render(request, "portfolio/index.html", {'categories': categories})

def list_category(request, id):
	categories = models.PortfolioCategory.objects.all()
	try:
		category = models.PortfolioCategory.objects.get(pk=id)
	except models.PortfolioCategory.DoesNotExist:
		return redirect('portfolio:mainindex')

	if category.name == 'Proprietary':
		items = models.ProprietaryPortfolioItem.objects.filter(category__exact=id)
	else:
		items = models.PortfolioItem.objects.filter(category__exact=id)
	return render(request, "portfolio/list_category.html", {'category': category, 'categories': categories, 'items': items})

def show_item(request, id):
	return HttpResponse("plerp")