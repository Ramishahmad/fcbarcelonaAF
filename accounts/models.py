from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
from django.utils.timesince import timesince

# Create your models here.



class AccountsModelManager(BaseUserManager):

    def create_user(self,name,email,gender, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            name = name,
            email = self.normalize_email(email),
            gender = gender
        )
        

        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = False
        user.save(using = self._db)
        return user


    def create_superuser(self,name,email,gender, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.create_user(
            name = name,
            email = self.normalize_email(email),
            gender = gender,
            password = password
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        # has_module_perms = True
        user.save(using = self._db)
        return user



class Accounts(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10, null=True,blank=True)
    image = models.ImageField(upload_to='profile',null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    # has_module_perms = models.BooleanField(default=False)

    objects = AccountsModelManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','gender']

    @property
    def age(self):
        if self.date_of_birth:
            return timesince(self.date_of_birth)
        else:
            return "Not Defined"

    def has_module_perms(self,self1):
        has_module_perms = True


    def __str__(self):
        return self.email