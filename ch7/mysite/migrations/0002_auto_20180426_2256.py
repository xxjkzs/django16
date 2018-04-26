# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nickname',
            field=models.CharField(verbose_name='摘要', max_length=15, default='Great Value Secondhand Phones'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pmodel',
            field=models.ForeignKey(verbose_name='型号', to='mysite.PModel'),
        ),
    ]
