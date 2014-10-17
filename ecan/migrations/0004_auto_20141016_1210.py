# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecan', '0003_remove_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_color',
            field=models.ImageField(default=datetime.date(2014, 10, 16), upload_to=b'items'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='image_ir',
            field=models.ImageField(default=datetime.date(2014, 10, 16), upload_to=b'recognition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
