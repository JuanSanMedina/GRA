# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0009_auto_20150325_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
