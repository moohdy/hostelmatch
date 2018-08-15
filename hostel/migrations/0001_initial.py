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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='created')),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('image1', models.ImageField(upload_to='hostel/%Y/%m/%d')),
                ('image2', models.ImageField(upload_to='hostel/%Y/%m/%d')),
                ('image3', models.ImageField(upload_to='hostel/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, upload_to='hostel/%Y/%m/%d')),
                ('image5', models.ImageField(blank=True, upload_to='hostel/%Y/%m/%d')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('vacant', models.BooleanField(default=True)),
                ('price', models.CharField(max_length=200)),
                ('created', models.DateField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
