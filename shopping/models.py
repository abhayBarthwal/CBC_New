from django.contrib.auth.models import User
from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class product(models.Model):
    name = models.CharField(max_length=300)
    cat = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
