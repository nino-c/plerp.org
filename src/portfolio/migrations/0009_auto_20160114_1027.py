# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20160114_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocategory',
            name='deployment_type',
            field=models.CharField(default='canvasapp', max_length=50, choices=[('canvasapp', 'HTML5 Canvas'), ('paper', 'Academic Papers'), ('sourcecode', 'Raw Source Code'), ('description', 'Description and gallery of images')]),
        ),
    ]
