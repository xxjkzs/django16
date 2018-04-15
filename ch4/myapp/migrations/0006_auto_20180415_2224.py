# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180415_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=1, choices=[('L', 'Large'), ('M', 'Medium'), ('S', 'Small')]),
        ),
    ]
