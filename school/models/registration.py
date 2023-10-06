from django.db import models
from .course import Course
from .student import Student


class Registration(models.Model):
    PERIOD_CHOICE = (
        # Matutino
        ('M', 'Morning'),
        # Vespertino
        ('A', 'Afternoon'),
        # Noturno
        ('N', 'Nocturnal'),
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    course_period = models.CharField(
        max_length=1,
        choices=PERIOD_CHOICE,
        blank=False,
        null=False,
        default='M'
    )
