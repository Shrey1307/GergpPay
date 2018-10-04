# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Name', models.CharField(max_length=1000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay.User')),
            ],
        ),
    ]
