# authentication/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q  # Add this import

class EmailMobileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()

        # Check if username is an email or mobile number
        user = User.objects.filter(Q(email=username) | Q(mobile_number=username)).first()

        if user and user.check_password(password):
            return user
        return None
