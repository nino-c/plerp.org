# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to=b'')),
                ('deployment_type', models.CharField(default='canvasapp', max_length=50, choices=[('canvasapp', 'HTML5 Canvas'), ('paper', 'Academic Paper'), ('sourcecode', 'Raw Source Code')])),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('sourcecode', models.URLField()),
            ],
        ),
    ]
