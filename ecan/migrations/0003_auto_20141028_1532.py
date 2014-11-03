# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0002_auto_20141028_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
