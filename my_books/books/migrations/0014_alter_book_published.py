# Generated by Django 4.2.2 on 2023-07-13 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 16, 25, 48, 594247, tzinfo=datetime.timezone.utc), verbose_name='Дата внесения в базу'),
        ),
    ]
