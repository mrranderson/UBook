# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UBook', '0002_auto_20151119_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubookprofile',
            name='cc_expdate',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
