# Generated by Django 4.2.2 on 2023-07-13 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 15, 29, 24, 250784, tzinfo=datetime.timezone.utc), verbose_name='Дата внесения в базу'),
        ),
    ]
