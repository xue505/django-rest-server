from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserProfileManager(BaseUserManager):
    """ UserProfile manager """

    def create_user(self, email, name, password=None):
        """ Creating a new UserProfile object"""

        if not email:
            raise ValueError('User must have a email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        """ Creating a new UserProfile superuser object """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """ when django convert object to string """

        return self.email


class ProfileFeedItem(models.Model):

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.status_text