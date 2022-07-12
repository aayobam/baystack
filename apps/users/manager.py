from django.contrib.auth.models import BaseUserManager
from django.forms import ValidationError



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValidationError("Email is required...")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff should be set to True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser should be set to True")
            
        if not email:
            raise ValueError("Email is required...")

        return self.create_user(email, password, **extra_fields)