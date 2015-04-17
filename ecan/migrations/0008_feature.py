# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecan', '0007_auto_20150318_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feat_name', models.CharField(max_length=255, null=True, blank=True)),
                ('feat_description', models.CharField(max_length=255, null=True, blank=True)),
                ('feature', picklefield.fields.PickledObjectField(editable=False)),
                ('item', models.ForeignKey(to='ecan.Item', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
