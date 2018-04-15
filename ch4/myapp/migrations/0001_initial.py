# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('bigint_f', models.BigIntegerField()),
                ('bool_f', models.BooleanField()),
                ('date_f', models.DateField(auto_now=True)),
                ('char_f', models.CharField(max_length=20, unique=True)),
                ('datetiem_f', models.DateTimeField(auto_now_add=True)),
                ('decimal_f', models.DecimalField(max_digits=10, decimal_places=2)),
                ('float_f', models.FloatField(null=True)),
                ('int_f', models.IntegerField(default=2018)),
                ('text_f', models.TextField()),
            ],
        ),
    ]
