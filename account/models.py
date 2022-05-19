from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, email, **kwargs):
        if not email:
            raise ValueError('the given email must be set')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

    def create_user(self, password, email, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(password, email, **kwargs)

    def create_superuser(self, password, email, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser')
        return self._create_user(password, email, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, )
    activation_code = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_active = models.BooleanField(_('active'), default=False, help_text='Designates whether this user should be treated as active.''Unselect this instead of deleting account')

    def __str__(self): return f'{self.email}'

    def create_activation_code(self):
        import uuid
        self.activation_code = str(uuid.uuid4())

