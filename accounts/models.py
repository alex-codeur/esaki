from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    phone = models.IntegerField(null=True, blank=True)
    image = CloudinaryField('image')
    
    def __str__(self):
        return f'{self.user.username} - Profile'