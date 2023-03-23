from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField(default=0)
    profilePic= models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
        img = Image.open(self.profilePic.path)
        if(img.height>100 or img.width >100):

            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.profilePic.path)
            



