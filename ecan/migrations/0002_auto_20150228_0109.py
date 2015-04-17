# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='test_train',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='back_ground',
            name='im',
            field=models.ImageField(upload_to=b'back_ground/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='im',
            field=models.ImageField(upload_to=b'pi_cam/'),
        ),
    ]
