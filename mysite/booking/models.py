from django.db import models
from django.contrib.auth.models import User
from clinics.models import Clinics
# Create your models here.


class Queues(models.Model):
    user = models.ForeignKey(User,related_name="user_name", on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinics,related_name="queue_name", on_delete=models.CASCADE)
    # max_patient = models.IntegerField( null=True, blank=True  )
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.clinic_name.name
