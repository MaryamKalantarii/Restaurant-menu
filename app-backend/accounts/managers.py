from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """ create custom user by phone number """

    def create_user(self, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError(_('شماره همراه اجباری است'))
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)
    