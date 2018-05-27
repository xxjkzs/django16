# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
