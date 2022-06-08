from django.db import models
#crreating default class for  Djanog User Model for overriding
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

#create the manager to manipulate the models
class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        """Create new User profile. If not email raise error"""
        if not email:
            raise ValueError('User must have email addr')
#Normalization of email for case sensitivity
        email=self.normalize_email(email)
#self.model if for reference which manager belongs to i.e. new model is created ith variable "user"
        user = self.model()
        user.set_password(password) #stored as hashed value
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """Create create_superuser .they should have password"""
        user=self.create_user(email,name,password)
        user.is_staff=True
        user.is_superuser=True #part of PermissionsMixin
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database models for users in systems"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    #isstaff--> wheth
    objects=UserProfileManager()
    """instead of username field we have overwritten with email field)"""
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Return full name  of user"""
        return self.name

    def get_short_name(self):
        return self.name

    """convert userprofile object to python"""
    def __str__(self):
        """Return string representation  of user"""
        return self.email
