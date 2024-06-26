from django.db import models

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(
        self,
        email,
        first_name,
        last_name,
        username,
        password=None,
        ):
        """
        Creates and saves a User with the given email, first_name,last_name,username and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),
                          username=username, first_name=first_name,
                          last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        username,
        password=None,
        ):
        """
        Creates and saves a superuser with the given email, first_name,last_name,username and password.
        """

        user = self.create_user(email, password=password,
                                username=username,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):

    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    username = models.CharField(unique=True,max_length=16)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        '''Does the user have a specific permission?'''

        # Simplest possible answer: Yes, always

        return self.is_admin

    def has_module_perms(self, app_label):
        '''Does the user have permissions to view the app `app_label`?'''

        # Simplest possible answer: Yes, always

        return True

    @property
    def is_staff(self):
        '''Is the user a member of staff?'''

        # Simplest possible answer: All admins are staff

        return self.is_admin
