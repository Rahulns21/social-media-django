from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Post(models.Model):
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.caption

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    caption = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, blank=True, editable=True)
    created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.caption != self._old_caption:
            self.slug = slugify(self.caption)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._old_caption = self.caption

@receiver(pre_save, sender=Post)
def update_post_slug(sender, instance, **kwargs):
    if instance.pk:
        instance._old_caption = Post.objects.get(pk=instance.pk).caption