from django.db import models

from django.contrib.auth.models import BaseUserManager
class AdminTableManager(BaseUserManager):
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user;
        

from django.contrib.auth.models import AbstractBaseUser
class AdminTable(AbstractBaseUser):
    userId = models.BigAutoField(primary_key=True)
    first_Name  = models.CharField(max_length=30)
    last_Name  = models.CharField(max_length=30)
    email = models.CharField(unique=True,max_length=100)
    is_superuser = models.BooleanField(default=True)

    objects = AdminTableManager()
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['first_Name','last_Name']
    