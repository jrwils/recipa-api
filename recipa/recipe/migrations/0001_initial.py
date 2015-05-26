# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
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
                ('url', models.CharField(max_length=40, db_index=True)),
                ('category', models.ManyToManyField(to='category.Category')),
                ('submitter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
