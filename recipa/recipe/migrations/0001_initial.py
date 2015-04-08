# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('category', models.ManyToManyField(to='category.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
