# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='UserProfile',
            fields=[
                ('profileid', models.AutoField(db_column='profileid', primary_key=True, serialize=False)),
                ('city', models.ForeignKey(db_column='cityid', to='submitter.City')),
                ('userid', models.ForeignKey(db_column='userid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='stateid', to='submitter.State'),
            preserve_default=True,
        ),
    ]
