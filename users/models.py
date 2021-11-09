from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager(BaseUserManager):
    # def create_user(self, login, password, **extra_fields):
    #     if not login:
    #         raise ValueError('Users must have an Login')
    #
    #     user = self.model(
    #         # email = self.normalize_email(email),
    #         login       = login,
    #         **extra_fields
    #     )
    #     user.set_password=(password)
    #     user.save()
    #     return user
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
# Create your models here.

class Account(AbstractBaseUser,PermissionsMixin):
    first_name          = models.CharField(max_length=70)
    last_name           = models.CharField(max_length=70)
    mobile_phone        = models.CharField(max_length=14)
    address             = models.CharField(max_length=100)
    email               = models.EmailField(verbose_name='email',max_length=70,unique=True)
    login               = models.CharField(verbose_name='login',max_length=70,unique=True)
    feed_id             = models.CharField(max_length=100)
    feed_id_access      = models.CharField(max_length=100)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['first_name','last_name','mobile_phone','address','email','feed_id',
                       'feed_id_access']


    def __str__(self):
        return self.login

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class Devices(models.Model):
    ESN         = models.CharField(max_length=100,unique=True)
    user        = models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.ESN
