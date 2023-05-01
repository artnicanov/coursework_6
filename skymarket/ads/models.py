from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(blank=True, null=True, max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads_images', null=True, blank=True)


class Comment(models.Model):
    text = models.TextField(null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

