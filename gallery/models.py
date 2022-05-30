
from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.

#location 
class Location(models.Model):
  location= models.CharField(max_length=100)

  def __str__(self):
    return self.location


#Category
class Category(models.Model):
  category= models.CharField(max_length=100)

  def __str__(self):
    return self.category




#Image

class Image(models.Model):
  image_att = CloudinaryField('image',blank=True,null=True)
  image_name = models.CharField(max_length=100)
  image_description = models.TextField(max_length=200)
  category = models.ForeignKey(Category,on_delete=models.DO_NOTHING, blank=True,null=True)
  location= models.ForeignKey(Location,on_delete=models.DO_NOTHING, blank=True, null=True)
  
  def __str__(self):
    return self.image_name
    
  def save_image(self):
    self.save()

  @classmethod
  def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category=search_term)
        return images
        

  class Meta:
    ordering = ['image_name']

 




  

