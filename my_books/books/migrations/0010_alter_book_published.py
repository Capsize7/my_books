# Generated by Django 4.2.2 on 2023-07-08 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_published_alter_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 14, 54, 40, 312950, tzinfo=datetime.timezone.utc), verbose_name='Дата внесения в базу'),
        ),
    ]