# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UBook', '0003_auto_20151119_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubookprofile',
            name='cc_type',
            field=models.CharField(default=1, max_length=20, choices=[(1, b'Visa'), (2, b'Mastercard'), (3, b'American Express'), (4, b'Discover')]),
        ),
    ]
