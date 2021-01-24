from django.db import models
from django.contrib.auth.models import User


class Clinics(models.Model):
    user = models.ForeignKey(User,related_name="clinic_nam", on_delete=models.CASCADE)
    name = models.CharField(max_length=30,  null=True, blank=True  )
    address = models.CharField(max_length=30,  null=True, blank=True  )
    phone = models.CharField(max_length=30,  null=True, blank=True  )
    max_patient = models.IntegerField( null=True, blank=True  )
    field = models.CharField(max_length=30,  null=True, blank=True  )
    image = models.ImageField(upload_to = 'clinics_images/',null=True, blank=True)
    def __str__(self):
        return self.name
