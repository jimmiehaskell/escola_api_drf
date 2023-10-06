from django.db import models


class Student(models.Model):
    name = models.CharField(
        max_length=50
    )
    personal_id = models.CharField(
        max_length=11
    )
    cpf = models.CharField(
        max_length=11
    )
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
