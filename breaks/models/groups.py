from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    organisation = models.ForeignKey(
        'breaks.Organisation', models.CASCADE, 'groups',
        verbose_name='Organisation'
    )
    name = models.CharField('Name', max_length=255)
    manager = models.ForeignKey(
        User, models.RESTRICT, 'group_managers',
        verbose_name='Manager'
    )
    employees = models.ManyToManyField(
        User, 'group_employees', verbose_name='Employees',
        blank=True
    )
    min_active = models.PositiveSmallIntegerField(
        'Minimum number of active employees', null=True, blank=True
    )
    break_start = models.TimeField('Start break', null=True, blank=True)
    break_end = models.TimeField('Break end', null=True, blank=True)
    break_max_duration = models.PositiveSmallIntegerField(
        'Minimum break duration', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def break_duration(self):
        return 500
