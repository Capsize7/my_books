# Generated by Django 4.2.2 on 2023-07-06 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 17, 35, 7, 2706, tzinfo=datetime.timezone.utc), verbose_name='Дата внесения в базу'),
        ),
    ]