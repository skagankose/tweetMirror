# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'unknownUser', max_length=200)),
                ('t1w1', models.CharField(default=b't1w1', max_length=200)),
                ('t1w2', models.CharField(default=b't1w2', max_length=200)),
                ('t1w3', models.CharField(default=b't1w3', max_length=200)),
                ('t1w4', models.CharField(default=b't1w4', max_length=200)),
                ('t1w5', models.CharField(default=b't1w5', max_length=200)),
                ('t1w6', models.CharField(default=b't1w6', max_length=200)),
                ('t1w7', models.CharField(default=b't1w7', max_length=200)),
                ('t2w1', models.CharField(default=b't2w1', max_length=200)),
                ('t2w2', models.CharField(default=b't2w2', max_length=200)),
                ('t2w3', models.CharField(default=b't2w3', max_length=200)),
                ('t2w4', models.CharField(default=b't2w4', max_length=200)),
                ('t2w5', models.CharField(default=b't2w5', max_length=200)),
                ('t2w6', models.CharField(default=b't2w6', max_length=200)),
                ('t2w7', models.CharField(default=b't2w7', max_length=200)),
                ('t3w1', models.CharField(default=b't2w1', max_length=200)),
                ('t3w2', models.CharField(default=b't2w2', max_length=200)),
                ('t3w3', models.CharField(default=b't2w3', max_length=200)),
                ('t3w4', models.CharField(default=b't2w4', max_length=200)),
                ('t3w5', models.CharField(default=b't2w5', max_length=200)),
                ('t3w6', models.CharField(default=b't2w6', max_length=200)),
                ('t3w7', models.CharField(default=b't2w7', max_length=200)),
            ],
        ),
    ]
