# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-02-23 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_taskinsession_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('atext', models.CharField(max_length=1000)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='student',
        ),
        migrations.RemoveField(
            model_name='session',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='taskinsession',
            name='session',
        ),
        migrations.RemoveField(
            model_name='taskinsession',
            name='task',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='TaskInSession',
        ),
    ]
