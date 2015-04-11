# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryid', models.AutoField(primary_key=True, db_column='categoryid', serialize=False)),
                ('categoryname', models.CharField(max_length=40)),
                ('categoryurl', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
