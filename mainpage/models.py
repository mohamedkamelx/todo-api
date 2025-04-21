from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# models.py
class Profile(models.Model):
    user = models.OneToOneField(  # Prevent multiple profiles
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
    )
    score = models.PositiveSmallIntegerField(default=0)  # Provide default value
    def __str__(self):
        return self.user.username
    

class Tasks(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description=models.TextField()
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='tasks')
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.title