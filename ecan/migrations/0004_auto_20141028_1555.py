# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0003_auto_20141028_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_picam',
            field=models.ImageField(upload_to=b'/media/picam_im'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_usb',
            field=models.ImageField(upload_to=b'/media/usb_im'),
        ),
    ]
