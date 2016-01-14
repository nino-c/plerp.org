# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20160114_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocategory',
            name='deployment_type',
            field=models.CharField(default='canvasapp', max_length=50, choices=[('canvasapp', 'HTML5 Canvas'), ('paper', 'Papers'), ('sourcecode', 'Raw Source Code'), ('description', 'Description and gallery of images')]),
        ),
    ]
