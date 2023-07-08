# Generated by Django 4.2.2 on 2023-07-07 14:40

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('books', '0008_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 7, 14, 40, 21, 778838, tzinfo=datetime.timezone.utc), verbose_name='Дата внесения в базу'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
    ]
