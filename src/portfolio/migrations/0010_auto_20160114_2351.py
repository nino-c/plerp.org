# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20160114_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanvasAppPortfolioItem',
            fields=[
                ('portfolioitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.PortfolioItem')),
                ('script', models.CharField(max_length=100)),
                ('script_type', models.CharField(max_length=10)),
            ],
            bases=('portfolio.portfolioitem',),
        ),
        migrations.AlterField(
            model_name='portfoliocategory',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
