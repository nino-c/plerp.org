# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_canvasappportfolioitem_appname'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvasappportfolioitem',
            name='deployment_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
