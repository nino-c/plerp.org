# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20160114_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvasappportfolioitem',
            name='script_type',
            field=models.CharField(max_length=100),
        ),
    ]
