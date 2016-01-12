from __future__ import unicode_literals

from django.db import models
import datetime


class PortfolioCategory(models.Model):

	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=100)
	description = models.TextField()
	icon = models.ImageField()
	deployment_type = models.CharField(max_length=50, 
		choices=(('canvasapp', 'HTML5 Canvas'), ('paper', 'Academic Paper'), ('sourcecode', 'Raw Source Code')),
		default='canvasapp')

class PortfolioItem(models.Model):

	def __unicode__(self):
		return self.title

	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=500, blank=True)
	category = models.ForeignKey(PortfolioCategory)
	description = models.TextField()
	sourcecode = models.URLField()