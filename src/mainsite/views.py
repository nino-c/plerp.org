from django.views import generic
from django.shortcuts import render

def index(request):
	return render(request, "home2.html")

class AboutPage(generic.TemplateView):
	template_name = "about.html"

