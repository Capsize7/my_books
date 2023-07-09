# Generated by Django 4.2.2 on 2023-07-06 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique_for_date=models.DateTimeField(auto_now_add=True)),
            preserve_default=False,
        ),
    ]