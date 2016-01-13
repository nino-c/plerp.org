# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_imagemodel_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='image',
            field=django_thumbs.db.models.ImageWithThumbsField(null=True, upload_to=b''),
        ),
    ]
