from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    form_completed = models.BooleanField(default=False)

class UpImg(models.Model):
    name = models.CharField(max_length=50)
    up_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
class EncKey(models.Model):
    my_key = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.my_key}'