# Generated by Django 4.2.2 on 2023-07-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_avatars.jpg', upload_to='profile_images', verbose_name='Аватарка'),
        ),
    ]