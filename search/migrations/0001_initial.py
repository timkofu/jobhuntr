# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('a2code', models.CharField(max_length=2)),
                ('continent', models.ForeignKey(to='search.Continent')),
            ],
        ),
        migrations.CreateModel(
            name='JobsData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('country', models.ForeignKey(to='search.Country')),
            ],
        ),
        migrations.AddField(
            model_name='jobsdata',
            name='source',
            field=models.ForeignKey(to='search.SourceLinks'),
        ),
    ]
