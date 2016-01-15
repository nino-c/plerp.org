# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20160115_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvasappportfolioitem',
            name='appname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
