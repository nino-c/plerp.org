from __future__ import unicode_literals


from django.db import models
from django.utils.timezone import now
from django_thumbs.db.models import ImageWithThumbsField




class PortfolioCategory(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    image = ImageWithThumbsField(null=True, sizes=((125,125),(200,200)))
    deployment_type = models.CharField(max_length=50, 
        choices=(
            ('canvasapp', 'HTML5 Canvas'), 
            ('paper', 'Academic Papers'), 
            ('sourcecode', 'Raw Source Code'),
            ('description', 'Description and gallery of images')),
        default='canvasapp')

class PortfolioItem(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(PortfolioCategory)
    description = models.TextField()
    sourcecode = models.URLField()
    image = ImageWithThumbsField(null=True, sizes=((125,125),(200,200)))
    year = models.IntegerField()
    month = models.IntegerField()



class ImageGallery(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

class ImageModel(models.Model):
    image = ImageWithThumbsField(sizes=((125,125),(200,200)))
    timestamp = models.DateTimeField(default=now, editable=False)
    gallery = models.ForeignKey(ImageGallery, null=True, related_name='images')



class ProprietaryPortfolioItem(PortfolioItem):

    def __init__(self, *args, **kwargs):
        super(ProprietaryPortfolioItem, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.title

    company = models.CharField(max_length=100)
    gallery = models.ForeignKey(ImageGallery)