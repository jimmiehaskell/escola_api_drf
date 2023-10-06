from rest_framework import serializers
from school.models import Registration


class StudentEnrollmentListSerialize(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    course_period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = [
            'course',
            'course_period',
        ]

    @staticmethod
    def get_course_period(obj):
        return obj.get_course_period_display()
