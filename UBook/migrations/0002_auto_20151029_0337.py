# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UBook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ubookprofile',
            old_name='zip_code',
            new_name='zipcode',
        ),
    ]
