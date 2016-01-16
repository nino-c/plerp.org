# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_canvasappportfolioitem_deployment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvasappportfolioitem',
            name='script_mime_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='canvasappportfolioitem',
            name='urlpath',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
