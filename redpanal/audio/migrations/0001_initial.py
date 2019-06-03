# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-28 22:43
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import redpanal.utils.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('description', models.TextField(verbose_name='description')),
                ('audio', models.FileField(max_length=250, upload_to=b'uploads/audios/%Y_%m', verbose_name='audio')),
                ('license', models.CharField(choices=[(b'CC-BY-SA-4.0', 'Creative Commons Attribution-ShareAlike 4.0 International')], default=b'CC-BY-SA-4.0', max_length=30, verbose_name='license')),
                ('genre', models.CharField(choices=[(b'pop', 'pop'), (b'rock', 'rock'), (b'jazz', 'jazz'), (b'blues', 'blues'), (b'folklore', 'folklore'), (b'electronic', 'electronic'), (b'other', 'other')], max_length=30, verbose_name='genre')),
                ('use_type', models.CharField(choices=[(b'track', 'track'), (b'loop', 'loop'), (b'song', 'song'), (b'sample', 'sample'), (b'other', 'other')], max_length=30, verbose_name='type')),
                ('instrument', models.CharField(choices=[(b'voice', 'voice'), (b'guitar', 'guitar'), (b'electric guitar', 'electric guitar'), (b'bass', 'bass'), (b'drums', 'drums'), (b'saxophone', 'saxophone'), (b'piano', 'piano'), (b'sinthesizer', 'sinthesizer'), (b'electronic', 'electronic'), (b'strings', 'other strings'), (b'woodwind', 'woodwind'), (b'brass', 'brass'), (b'multiple', 'multiple'), (b'other', 'other')], max_length=30, verbose_name='instrument')),
                ('channels', models.IntegerField(editable=False, null=True)),
                ('blocksize', models.IntegerField(editable=False, null=True)),
                ('samplerate', models.IntegerField(editable=False, null=True)),
                ('totalframes', models.IntegerField(editable=False, null=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='hashtags')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'audio',
                'verbose_name_plural': 'audios',
            },
            bases=(models.Model, redpanal.utils.models.BaseModelMixin),
        ),
    ]