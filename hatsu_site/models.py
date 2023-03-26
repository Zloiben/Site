from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d",
                              default="photos/default_image_blog.jpg", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    is_pinned = models.BooleanField(default=False, verbose_name="Закреплен")
    likes = models.IntegerField(default=0, verbose_name="Лайков")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создал")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return f"Post. title: {self.title} slug: {self.slug}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def get_total_likes(self):
        return len(Like.objects.all().filter(post=self.pk))

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f"Category. name: {self.name} slug: {self.slug}"

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['id']


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Поставил")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Поставил в")

    def __str__(self):
        return f"Like. post: {self.post.title} author: {self.author}"

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = "Лайки"
        ordering = ['id']


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Поставил")
    image = models.ImageField(upload_to="photos/%Y/%m/%d",
                              default="photos/default_image_profile.svg", verbose_name="Фото")

    def __str__(self):
        return f"UserProfile. author={self.user}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = "Профиля"
        ordering = ['id']
