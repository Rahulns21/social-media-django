from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return self.user.username

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)