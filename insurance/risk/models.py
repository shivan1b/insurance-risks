# Standard Library
from enum import Enum

# Third Party Stuff
from django.db import models

# Django Dynamic Models Stuff
from insurance.base.models import TimeStampedUUIDModel


class Risk(TimeStampedUUIDModel):
    name = models.CharField(max_length=200)
    insurer = models.ForeignKey('users.User')

    class Meta:
        ordering = ['-created']
        default_related_name = 'risks'
        db_table = 'risks'

    def __str__(self):
        return str(self.name)


class RiskField(TimeStampedUUIDModel):
    class FTYPE(Enum):
        char_f = ('ch', 'String')
        int_f = ('in', 'Integer')
        datetime_f = ('dt', 'DateTime')
        choice_f = ('en', 'Choices')

        @classmethod
        def get_val(cls, ftype):
            return cls[ftype].value[0]

    risk = models.ForeignKey(Risk)
    name = models.CharField(max_length=200)
    ftype = models.CharField(
        max_length=2,
        choices=[x.value for x in FTYPE],
        help_text='Type of the field.')

    class Meta:
        ordering = ['-created']
        default_related_name = 'riskfields'
        db_table = 'riskfields'

    def __str__(self):
        return str(self.name)
