# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0011_auto_20150325_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumb',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
            preserve_default=True,
        ),
    ]
