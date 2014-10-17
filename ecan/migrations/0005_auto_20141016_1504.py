# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0004_auto_20141016_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_color',
            field=models.ImageField(upload_to=b'color_im'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_ir',
            field=models.ImageField(upload_to=b'ir_im'),
        ),
    ]
