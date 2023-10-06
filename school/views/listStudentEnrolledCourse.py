from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Registration
from school.serializers import ListStudentsEnrolledCourseSerializer


class ListStudentEnrolledCourse(generics.ListAPIView):
    """ Displays all students enrolled in a course """
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])

        return queryset

    serializer_class = ListStudentsEnrolledCourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
