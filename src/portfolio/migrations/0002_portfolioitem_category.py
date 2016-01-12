# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='category',
            field=models.ForeignKey(default=1, to='portfolio.PortfolioCategory'),
            preserve_default=False,
        ),
    ]
