from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30,  null=True, blank=True  )
    phone = models.CharField(max_length=30,  null=True, blank=True  )
    cell_phone = models.CharField(max_length=30,  null=True, blank=True  )
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.FileField(upload_to='avatar',null=True,blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ClinicProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,  null=True, blank=True  )
    address = models.CharField(max_length=30,  null=True, blank=True  )
    phone = models.CharField(max_length=30,  null=True, blank=True  )
    avatar = models.FileField(upload_to='clinic_image',null=True,blank=True)
    def __str__(self):
        return self.name
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        ClinicProfile.objects.create(user=instance)
    instance.clinicprofile.save()
