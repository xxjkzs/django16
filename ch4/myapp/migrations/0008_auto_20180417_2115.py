# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180417_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=1, choices=[('L', 'Large'), ('M', 'Medium'), ('S', 'Small')]),
        ),
    ]
