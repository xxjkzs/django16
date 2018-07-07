# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=filer.fields.image.FilerImageField(to=settings.FILER_IMAGE_MODEL, related_name='product_image'),
        ),
    ]
