from django.db import models
from users.models import *


class MedicalReport(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    report_id = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    report_file = models.FileField(upload_to='medical_reports/')

    def __str__(self):
        return self.report_id
