from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User,related_name="post_user", on_delete=models.CASCADE)
    product_code = models.CharField(max_length=30,  null=True, blank=True  )
    name = models.CharField(max_length=30,  null=True, blank=True  )
    provider = models.CharField(max_length=30,  null=True, blank=True  )
    price = models.IntegerField( null=True, blank=True  )
    image = models.ImageField(upload_to = 'product_images/',null=True, blank=True)
    def __str__(self):
        return self.name
