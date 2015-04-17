# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0003_auto_20150316_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, to='ecan.Brand', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='material',
            field=models.ForeignKey(blank=True, to='ecan.Material', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='shape',
            field=models.ForeignKey(blank=True, to='ecan.Shape', null=True),
        ),
    ]
