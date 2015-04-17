# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0008_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='feat_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='feat_name',
            new_name='name',
        ),
    ]
