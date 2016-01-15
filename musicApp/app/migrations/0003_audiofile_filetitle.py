# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160115_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='fileTitle',
            field=models.CharField(default=b'MP3 File', max_length=b'200'),
        ),
    ]
