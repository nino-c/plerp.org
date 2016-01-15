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

def get_categories():
    categories = models.PortfolioCategory.objects.all()
    return categories


##############################################
### views



def mainindex(request):
    categories = models.PortfolioCategory.objects.all()
    return render(request, "index.html", {'categories': categories, 'iframe_app': 'fractal_tree'})

def iframe(request, appname):
    template_name = "iframe.html"
    return render(request, "iframe.html", {'appname': appname})

# def index(request):
#   categories = models.PortfolioCategory.objects.all()
#   return render(request, "portfolio/index.html", {'categories': categories})



def list_category(request, id):
    try:
        category = models.PortfolioCategory.objects.get(pk=id)
    except models.PortfolioCategory.DoesNotExist:
        #return redirect('portfolio:mainindex')
        raise Exception("Category could not be found")

    if category.name == 'Proprietary':
        items = models.ProprietaryPortfolioItem.objects.filter(category__exact=id)
    else:
        items = models.PortfolioItem.objects.filter(category__exact=id)
    return render(request, "portfolio/list_category.html", {'category': category, 'categories': get_categories(), 'items': items})

def show_item(request, id):
    try:
        item = models.PortfolioItem.objects.get(pk=id)
    except models.PortfolioItem.DoesNotExist:
        #return redirect('portfolio:mainindex')
        raise Exception("Item could not be found")

    #categories = self.get_category()
    if item.category.deployment_type == 'canvasapp':
        try:
            item = models.CanvasAppPortfolioItem.objects.get(pk=id)
        except models.CanvasAppPortfolioItem.DoesNotExist:
            #return redirect('portfolio:mainindex')
            raise Exception("Item could not be found")
        #item.script = "{% static '"+ item.script +"' %}"
        return render(request, "portfolio/show_item.html", {'categories': get_categories, 'item': item})

    raise Exception("Neen needs to learn 404 response")

