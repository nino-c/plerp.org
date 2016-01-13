from django.views import generic
from django.shortcuts import render

def index(request):
	return render(request, "dashboard.html")

class AboutPage(generic.TemplateView):
	template_name = "about.html"

