from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

from crispy_forms.helper import *
from crispy_forms.layout import *

from . import models
from fractal_tree.views import FractalTreeForm


class Canvas:
    
    def __init__(self, script, script_type):
        self.script = script
        self.script_type = script_type

class InteractiveCanvas(Canvas):

    def __init__(self, *args, **kwargs):
        super(InteractiveCanvas, self).__init__(*args, **kwargs)
        self.control_panel = FractalTreeForm()



### views

def mainindex(request):
    categories = models.PortfolioCategory.objects.all()
    return render(request, "index.html", {'categories': categories})

# def index(request):
#   categories = models.PortfolioCategory.objects.all()
#   return render(request, "portfolio/index.html", {'categories': categories})

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
    try:
        item = models.PortfolioItem.objects.get(pk=id)
    except models.PortfolioItem.DoesNotExist:
        return redirect('portfolio:mainindex')

    if item.category.deployment_type == 'canvasapp':
        canvas = InteractiveCanvas()

    # return ??