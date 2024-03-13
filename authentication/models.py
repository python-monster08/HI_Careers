# authentication/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, mobile_number, password=None, **extra_fields):
        if not email and not mobile_number:
            raise ValueError(_('The Email or Mobile Number field must be set'))
        email = self.normalize_email(email) if email else None
        mobile_number = self.normalize_mobile_number(mobile_number) if mobile_number else None

        user = self.model(email=email, mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, mobile_number, password, **extra_fields)

    def normalize_mobile_number(self, mobile_number):
        # Implement any normalization logic for mobile numbers if needed
        return mobile_number

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add your additional fields for each user type (admin, teacher, student)
    # For example:
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Use 'email' as the default field for authentication
    REQUIRED_FIELDS = ['mobile_number']  # Additional fields required for create_user

    def __str__(self):
        return self.email or self.mobile_number  # Display either email or mobile number

    def get_full_name(self):
        return self.email or self.mobile_number  # Display either email or mobile number

    def get_short_name(self):
        return self.email or self.mobile_number  # Display either email or mobile number

    def normalize_mobile_number(self, mobile_number):
        # Implement any normalization logic for mobile numbers if needed
        return mobile_number
