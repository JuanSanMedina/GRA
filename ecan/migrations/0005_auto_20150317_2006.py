# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0004_auto_20150317_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='material',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='shape',
            old_name='shape',
            new_name='value',
        ),
    ]
