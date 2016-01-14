from django.views import generic
from django.shortcuts import render, redirect


def index(request):
	#categories = PortfolioCategory.objects.all()
	#return render(request, "home2.html", {'categories': categories})
	return redirect('portfolio:mainindex')

class AboutPage(generic.TemplateView):
	template_name = "about.html"
