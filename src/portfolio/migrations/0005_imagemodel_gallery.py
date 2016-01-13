# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_imagegallery_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='gallery',
            field=models.ForeignKey(related_name='images', to='portfolio.ImageGallery', null=True),
        ),
    ]
