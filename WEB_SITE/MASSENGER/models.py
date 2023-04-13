from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class PPL(models.Model):

    Kinds = (
        ('Ищу работу', 'Ищу работу'),
        ('Ищу работника', 'Ищу работника'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, verbose_name = 'Пользователь')
    first_name = models.CharField(max_length = 40, verbose_name = 'Имя')
    last_name = models.CharField(max_length = 40, verbose_name = 'Фамилия')
    surname = models.CharField(max_length = 40, verbose_name = 'Отчество/Матчество')
    age = models.IntegerField(null = True, blank = True, verbose_name = 'Возраст')
    profession = models.CharField(max_length = 100, verbose_name = 'Профессия')
    what_are_you_looking = models.CharField(max_length = 30, choices = Kinds, help_text = 'Введите вид поиска', default = 'JOB', verbose_name = 'Что ищет')
    region = models.ForeignKey('Region', null = True, blank = True, db_index = True, on_delete = models.CASCADE, verbose_name = 'Регион')
    image = models.ImageField(upload_to = 'images', max_length=100, null = True, blank = True, default = '/images/default.jpg' ,verbose_name = 'Фотография')
    information_about_skills = models.TextField(help_text = 'Введите информацию о своих HARDS SKILLS.', null = True, blank = True, default = 'Записей нет.', verbose_name = 'Информация о себе и об своих проффесиональных способностях')
    date_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Время создания')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ('first_name',)


class Region(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Регион')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'

