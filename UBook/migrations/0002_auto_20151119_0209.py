# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UBook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubookprofile',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='ubookprofile',
            name='cc_ccv',
            field=models.CharField(max_length=3, blank=True),
        ),
        migrations.AddField(
            model_name='ubookprofile',
            name='cc_expdate',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='ubookprofile',
            name='cc_number',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='ubookprofile',
            name='cc_type',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='ubookprofile',
            name='zipcode',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ubookprofile',
            name='address',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ubookprofile',
            name='city',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ubookprofile',
            name='state',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
