# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0005_auto_20141016_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecan',
            name='ip',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
