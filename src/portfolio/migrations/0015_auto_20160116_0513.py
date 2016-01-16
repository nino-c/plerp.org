# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20160116_0332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='canvasappportfolioitem',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='canvasappportfolioitem',
            name='appname',
        ),
        migrations.RemoveField(
            model_name='canvasappportfolioitem',
            name='deployment_name',
        ),
        migrations.RemoveField(
            model_name='canvasappportfolioitem',
            name='script',
        ),
        migrations.RemoveField(
            model_name='canvasappportfolioitem',
            name='script_type',
        ),
    ]
