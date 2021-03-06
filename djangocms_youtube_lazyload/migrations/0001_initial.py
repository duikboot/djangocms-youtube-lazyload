# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeLazyload',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=150, verbose_name='Title', blank=True)),
                ('thumbnail', models.FileField(help_text='Image Overlay - this image will display over the video on your site and allow users to see an image of your choice before playing the video.', upload_to='djangocms_youtube_lazyload', null=True, verbose_name='Custom Thumbnail', blank=True)),
                ('video_url', models.URLField(help_text='Paste the URL of the YouTube video', verbose_name='Video URL')),
                ('width', models.PositiveIntegerField(help_text='Sets the width of your player, used on some templates where applicable', null=True, verbose_name='Width', blank=True)),
                ('height', models.PositiveIntegerField(help_text='Sets the height of your player, used on some templates where applicable', null=True, verbose_name='Height', blank=True)),
                ('description', models.TextField(help_text='You can add a Description to your video, to be displayed beneath your video on your page.', null=True, verbose_name='Video Description', blank=True)),
                ('description_option', models.CharField(default=b'hidden', max_length=50, verbose_name='Description Option', blank=True, choices=[(b'hidden', 'Do Not Display Description'), (b'below', 'Description Below the Video')])),
                ('theme', models.CharField(default=b'light', max_length=100, verbose_name='Colorscheme controls', choices=[(b'dark', 'Dark'), (b'light', 'Light')])),
                ('plugin_template', models.CharField(default=b'djangocms_youtube_lazyload/video.html', max_length=255, verbose_name='Template', choices=[(b'djangocms_youtube_lazyload/default.html', 'Default')])),
                ('video_data', jsonfield.fields.JSONField(help_text='For advanced users only \u2014 please do not edit this data unless you know what you are doing.', null=True, verbose_name='YouTube Data', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
