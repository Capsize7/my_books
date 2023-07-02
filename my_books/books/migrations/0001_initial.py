# Generated by Django 4.2.2 on 2023-07-02 11:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('author', models.CharField(max_length=250)),
                ('photo', models.ImageField(default='default_books.jpg', upload_to='books_images')),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField()),
                ('written', models.IntegerField()),
                ('status', models.CharField(choices=[('RD', 'READ'), ('WR', 'WANT_TO_READ')], default='RD', max_length=2)),
                ('rating', models.IntegerField()),
                ('published', models.DateTimeField(default=datetime.datetime(2023, 7, 2, 11, 6, 15, 914755, tzinfo=datetime.timezone.utc))),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='books.genre')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['title', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book')),
            ],
            options={
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='books_comme_created_a3990d_idx')],
            },
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title', 'author'], name='books_book_title_b7b426_idx'),
        ),
    ]
