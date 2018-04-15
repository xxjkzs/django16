# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180415_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=1, choices=[('M', 'Medium'), ('L', 'Large'), ('S', 'Small')]),
        ),
    ]
