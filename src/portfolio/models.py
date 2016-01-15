from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django_thumbs.db.models import ImageWithThumbsField

from mainsite.settings.base import DEPLOYMENT_CHOICES




class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    image = ImageWithThumbsField(null=True, sizes=((125,125),(200,200)))
    deployment_type = models.CharField(max_length=50, choices=DEPLOYMENT_CHOICES, default='canvasapp')

    def __unicode__(self):
        return self.name

    def num_items(self):
        items = PortfolioItem.objects.filter(category__id=self.id)
        return len(items)

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(PortfolioCategory)
    description = models.TextField()
    sourcecode = models.URLField()
    image = ImageWithThumbsField(null=True, sizes=((125,125),(200,200)))
    year = models.IntegerField()
    month = models.IntegerField()

    def __unicode__(self):
        return self.title


class ImageGallery(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class ImageModel(models.Model):
    image = ImageWithThumbsField(sizes=((125,125),(200,200)))
    timestamp = models.DateTimeField(default=now, editable=False)
    gallery = models.ForeignKey(ImageGallery, null=True, related_name='images')



class ProprietaryPortfolioItem(PortfolioItem):

    company = models.CharField(max_length=100)
    gallery = models.ForeignKey(ImageGallery)

    def __init__(self, *args, **kwargs):
        super(ProprietaryPortfolioItem, self).__init__(*args, **kwargs)



class CanvasAppPortfolioItem(PortfolioItem):

    script = models.CharField(max_length=100)
    script_type = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(CanvasAppPortfolioItem, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.title

    