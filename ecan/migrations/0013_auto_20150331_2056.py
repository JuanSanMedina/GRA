# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0012_item_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='item',
            field=models.ForeignKey(to='ecan.Item'),
        ),
    ]
