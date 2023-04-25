from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False,null=True)

    
    class Meta:
        db_table = 'user'
        
