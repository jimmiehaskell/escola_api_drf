from rest_framework import serializers
from school.models import Registration


class ListStudentsEnrolledCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = [
            'student',
        ]
