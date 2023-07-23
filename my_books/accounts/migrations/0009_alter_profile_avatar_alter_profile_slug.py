# Generated by Django 4.2.2 on 2023-07-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_avatar.jpg', upload_to='profile_images', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(unique_for_date='created', verbose_name='Слаг'),
        ),
    ]
