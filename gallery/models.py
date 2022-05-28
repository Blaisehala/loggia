
from django.db import models



# Create your models here.

#location 
class Location(models.Model):
  location_name = models.CharField(max_length=100)

  def __str__(self):
    return self.location_name


#Category
class Category(models.Model):
  category_name = models.CharField(max_length=100)

  def __str__(self):
    return self.category_name




#Image

class Image(models.Model):
  image_name = models.CharField(max_length=100)
  image_description = models.TextField(max_length=200)
  
  def __str__(self):
    return self.image_name
    
  def save_image(self):
    self.save()

  @classmethod
  def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__category_name__icontains=image_category)
        return images
        

  class Meta:
    ordering = ['image_name']

 




  

