from django.contrib import admin
from portfolio.models import *

admin.site.site_title = "plerp.org"
admin.site.site_header = "plerp.org"

admin.site.register(PortfolioCategory)
admin.site.register(PortfolioItem)

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
# 	date_heirarchy = 'gamedate'