from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    avatar = models.ImageField(default='profile_images/default_avatar.jpg', upload_to='profile_images', verbose_name="Аватарка")
    bio = models.TextField(verbose_name="Общая информация")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    slug = models.SlugField(unique_for_date='created', verbose_name="Слаг")

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    class Meta:
        verbose_name = 'Профили'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
