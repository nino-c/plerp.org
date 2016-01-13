# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolioitem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', django_thumbs.db.models.ImageWithThumbsField(upload_to=b'')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProprietaryPortfolioItem',
            fields=[
                ('portfolioitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.PortfolioItem')),
                ('company', models.CharField(max_length=100)),
                ('gallery', models.ForeignKey(to='portfolio.ImageGallery')),
            ],
            bases=('portfolio.portfolioitem',),
        ),
        migrations.AddField(
            model_name='portfoliocategory',
            name='image',
            field=django_thumbs.db.models.ImageWithThumbsField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='year',
            field=models.IntegerField(default=2015),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfoliocategory',
            name='deployment_type',
            field=models.CharField(default='canvasapp', max_length=50, choices=[('canvasapp', 'HTML5 Canvas'), ('paper', 'Academic Paper'), ('sourcecode', 'Raw Source Code'), ('description', 'Description and gallery of images')]),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='subtitle',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='imagegallery',
            name='images',
            field=models.ManyToManyField(to='portfolio.ImageModel'),
        ),
    ]
