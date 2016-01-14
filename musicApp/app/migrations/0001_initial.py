# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fileDescription', models.TextField(default=b'', null=True, blank=True)),
                ('audioFile', models.FileField(upload_to=b'files/')),
                ('slugText', models.SlugField(max_length=100, null=True, blank=True)),
                ('fileOwner', models.ForeignKey(to='userprofile.UserProfile')),
            ],
        ),
    ]
