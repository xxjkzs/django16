# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180415_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=1, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]),
        ),
    ]
