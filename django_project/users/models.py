from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #"CASCADE" if user deleted delete profile
                                                                #if profile deleted don't delete user 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)#directory the img get uploaded to

    def __str__(self):
        return f'{self.user.username} Profile'
