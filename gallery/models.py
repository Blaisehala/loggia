from django.db import models

# Create your models here.

class Image(models.Model):
  image_name = models.CharField(max_length=100)
  image_description = models.TextField(max_length=200)
  image_location = models.ForeignKey()
  image_category = models.ForeignKey()
