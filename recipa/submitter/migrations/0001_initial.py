# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityid', models.AutoField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('stateid', models.AutoField(primary_key=True, serialize=False)),
                ('stateshort', models.CharField(max_length=2)),
                ('statelong', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submitter',
            fields=[
                ('submitterid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('city', models.ForeignKey(to='submitter.City', db_column='cityid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='submitter.State', db_column='stateid'),
            preserve_default=True,
        ),
    ]
