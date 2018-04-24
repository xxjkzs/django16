# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default='http://i.imgur.com/Ous4iGB.png')),
                ('maker', models.ForeignKey(to='mysite.Maker')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('discription', models.CharField(max_length=20, default='Product Photo')),
                ('url', models.URLField(default='http://i.imgur.com/Z230eeq.png')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nickname', models.CharField(max_length=15, default='Great Value Secondhand Phones')),
                ('discription', models.TextField(default='N/A')),
                ('year', models.PositiveIntegerField(default=2018)),
                ('price', models.PositiveIntegerField(default=0)),
                ('pmodel', models.ForeignKey(to='mysite.PModel')),
            ],
        ),
        migrations.AddField(
            model_name='pphoto',
            name='product',
            field=models.ForeignKey(to='mysite.Product'),
        ),
    ]
