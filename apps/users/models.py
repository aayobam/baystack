from django.utils.text import slugify
from django.db import models
from .manager import CustomUserManager
from apps.common.utils import TimeSTampsModel
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, TimeSTampsModel):
    email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True, blank=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ('email',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def generate_random_slug(self):
        random_slug = slugify(self.first_name + self.last_name + str(self.id))
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(self.first_name + self.last_name + self.id)
        return random_slug
            

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_random_slug()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email