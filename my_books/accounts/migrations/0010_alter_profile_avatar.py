# Generated by Django 4.2.2 on 2023-07-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_avatar_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile_images/default_avatar.jpg', upload_to='profile_images', verbose_name='Аватарка'),
        ),
    ]
