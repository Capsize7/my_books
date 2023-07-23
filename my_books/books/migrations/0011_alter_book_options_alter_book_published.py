# Generated by Django 4.2.2 on 2023-07-09 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-rating'], 'verbose_name': 'Книги', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 8, 3, 24, 216468, tzinfo=datetime.timezone.utc), verbose_name='Дата внесения в базу'),
        ),
    ]
