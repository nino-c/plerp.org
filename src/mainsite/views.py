from django.views import generic


class AboutPage(generic.TemplateView):
	template_name = "about.html"

