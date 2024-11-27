from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Table(models.Model):
    number = models.IntegerField(unique=True, verbose_name='Номер столика')
    capacity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Вместимость'
    )

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'

    def __str__(self):
        return f'Столик {self.number} (вместимость: {self.capacity})'

class Reservation(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    guests = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Количество гостей'
    )
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Столик')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f'Бронь {self.name} на {self.date} {self.time}' 