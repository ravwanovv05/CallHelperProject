from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organisation(models.Model):
    name = models.CharField('Name', max_length=255)
    director = models.ForeignKey(
        User, models.RESTRICT, 'organisations_directors',
        verbose_name='Director'
    )
    employees = models.ManyToManyField(
        User, 'organisations_employees', verbose_name='Employees',
        blank=True
    )

    class Meta:
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'
        ordering = ('name',)

    def __str__(self):
        return self.name


