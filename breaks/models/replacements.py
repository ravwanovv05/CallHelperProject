from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField(verbose_name='Code', max_length=16, primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=32,)
    sort = models.PositiveSmallIntegerField(verbose_name='Sort', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    class Meta:
        verbose_name = 'Replacement Status'
        verbose_name_plural = 'Replacements, Status'
        ordering = ('sort',)

    def __str__(self):
        return f'{self.code} for {self.name}'


class Replacement(models.Model):
    group = models.ForeignKey(
        'breaks.Group', models.CASCADE, 'replacements',
        verbose_name='Group'
    )
    date = models.DateField(verbose_name='Date of shift')
    break_start = models.TimeField(verbose_name='Start break')
    break_end = models.TimeField(verbose_name='End break')
    break_max_duration = models.PositiveIntegerField(
        verbose_name='Max. Duration of lunch'
    )

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        ordering = ('-date',)

    def __str__(self):
        return f'Shift №{self.pk} for {self.group.name}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        User, models.CASCADE, related_name='replacements',
        verbose_name='Employee'
    )
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, related_name='employees',
        verbose_name='Replacement'
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', models.RESTRICT, related_name='replacement_employees',
        verbose_name='Status'
    )

    class Meta:
        verbose_name = 'Replacement - Employee'
        verbose_name_plural = 'Replacements - Employees'

    def __str__(self):
        return f'Shift {self.replacement} for {self.employee}'
