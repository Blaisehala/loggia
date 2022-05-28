from django.test import TestCase
from .models import Image, Location, Category


# Create your tests here.

class ImageTestCase(TestCase):

  #set up method 
   def setUp(self):
     self.img1=Image(image_name='art', image_description='New_York')

   #testing instance
   def test_instance(self):
     self.assertTrue(self.img1,Image)

    
     
   def test_save_method(self):
     self.image.save_image()
     images = Image.objects.all()
     self.assertTrue(len(images)>0)

  

