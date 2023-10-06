from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Registration, Student
from school.serializers import StudentEnrollmentListSerialize


class StudentEnrollmentList(generics.ListAPIView):
    """ Display student enrollment list """
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])

        return queryset

    serializer_class = StudentEnrollmentListSerialize
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
