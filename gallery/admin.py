from django.contrib import admin
from gallery.models import Image, Location, Category

# Register your models here.

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
