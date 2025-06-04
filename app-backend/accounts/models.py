from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Custum User Model """

    class UserType(models.TextChoices):
        CUSTOMER = "customer", _("مشتری")
        RESTAURANT_OWNER  = "restaurant_owner", _("مدیر رستوران")

    user_type = models.CharField(_("نوع کاربر"), max_length=60, choices=UserType, default=UserType.CUSTOMER)
    phone_number = models.CharField(_("شماره همراه"), max_length=11, unique=True)
    date_join = models.DateTimeField(_("تاریخ ایجاد"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.phone_number} ({self.user_type})"
    

    class Meta:
        verbose_name = _("کاربر")
        verbose_name_plural = _("کاربران")
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    


class RestaurantOwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("کاربر"))
    owner_name = models.CharField(_("نام مدیر"), max_length=350, null=True, blank=True)
    address = models.CharField(_("آدرس"), max_length=500, null=True, blank=True)
    # restaurant = models.OneToOneField('Restaurant', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.owner_name
    

    class Meta:
        verbose_name = _("مدیر رستوران")
        verbose_name_plural = _("مدیران رستوران ها")
        