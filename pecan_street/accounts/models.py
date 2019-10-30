from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.utils import timezone

# Create your models here.
class Artist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


class TattooImage(models.Model):
    user = models.ForeignKey(Artist, related_name='tattoo_image', on_delete=models.PROTECT)
    image = ProcessedImageField(upload_to='tattoo_images', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='tattoo_images', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80})
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

