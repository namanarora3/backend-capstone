from .models import MedicalReport
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicalReportSerializer
from .models import MedicalReport
from rest_framework import generics
from .serializers import MedicalReportSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UploadFileView(generics.CreateAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetFileListView(generics.ListAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicalReport.objects.filter(user=self.request.user)


class GetFileView(generics.RetrieveAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
