from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = ProcessedImageField(upload_to='images/thumbnail/',
                                    processors=[Thumbnail(100, 100)],
                                    format='JPEG',
                                    options={'quality': 60},
                                    null=True
                                    )
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)
