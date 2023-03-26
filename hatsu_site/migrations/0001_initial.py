# Generated by Django 4.1.7 on 2023-03-20 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('photo', models.ImageField(default='static/image/default_image_blog.jpg', upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='Закреплен')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайков')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hatsu_site.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
