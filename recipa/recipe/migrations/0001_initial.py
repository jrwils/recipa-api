# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('submitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipeid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('intro', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('endcomments', models.TextField(blank=True)),
                ('url', models.CharField(db_index=True, max_length=40)),
                ('category', models.ManyToManyField(to='category.Category')),
                ('submitter', models.ForeignKey(to='submitter.Submitter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
