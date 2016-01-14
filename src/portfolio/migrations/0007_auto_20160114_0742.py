# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolioitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliocategory',
            name='icon',
        ),
        migrations.AddField(
            model_name='portfoliocategory',
            name='short_description',
            field=models.TextField(null=True),
        ),
    ]
