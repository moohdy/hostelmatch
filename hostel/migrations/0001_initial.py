# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique_for_date='created', max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('image1', models.ImageField(upload_to='hostel/%Y/%m/%d')),
                ('image2', models.ImageField(upload_to='hostel/%Y/%m/%d')),
                ('image3', models.ImageField(upload_to='hostel/%Y/%m/%d')),
                ('image4', models.ImageField(upload_to='hostel/%Y/%m/%d', blank=True)),
                ('image5', models.ImageField(upload_to='hostel/%Y/%m/%d', blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('vacant', models.BooleanField(default=True)),
                ('price', models.CharField(max_length=200)),
                ('created', models.DateField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
