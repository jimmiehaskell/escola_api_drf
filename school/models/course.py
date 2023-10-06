from django.db import models


class Course(models.Model):
    LEVEL_CHOICE = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced')
    )
    course_code = models.CharField(
        max_length=10
    )
    description = models.CharField(
        max_length=100
    )
    level = models.CharField(
        blank=False,
        choices=LEVEL_CHOICE,
        default='B',
        max_length=1,
        null=False
    )

    def __str__(self):
        return self.description
