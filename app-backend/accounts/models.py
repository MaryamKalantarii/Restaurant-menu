from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .validators import validate_iranian_cellphone_number

class UserType(models.IntegerChoices):
    customer = 1, _("customer")
    admin = 2, _("admin")
    superuser = 3, _("superuser")


class CustomeBaseUserManager(BaseUserManager):

    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("type", UserType.superuser.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_verified") is not True:
            raise ValueError("Superuser must have is_verified=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)
    
class CustomeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    type = models.IntegerField(
        choices=UserType.choices, default=UserType.customer.value)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomeBaseUserManager()

    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile/", default="profile/default.png")
    phone_number = models.CharField(max_length=20, validators=[validate_iranian_cellphone_number])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_fullname(self):
        full = f"{self.first_name} {self.last_name}".strip()
        return full if full else "کاربر جدید"

    def __str__(self):
        return self.get_fullname() or self.user.email
