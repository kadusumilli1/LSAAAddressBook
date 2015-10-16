# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('address', models.TextField(max_length=10)),
            ],
        ),
    ]
