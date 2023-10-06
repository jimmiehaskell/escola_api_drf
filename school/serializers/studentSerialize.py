from rest_framework import serializers
from school.models import Student


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'personal_id',
            'cpf',
            'date_of_birth'
        ]
