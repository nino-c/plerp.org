from django.shortcuts import render

# Create your views here.
def index(request):
	return render("general_iframe_js.html", {'iframe_app':'maze2d'})