from django.http  import HttpResponse
from django.shortcuts import render
from gallery.models import Image, Location, Category, Category


# Create your views here.
def gallery(request):
  images= Image.objects.all()
  location= Location.objects.all()
  
  return render(request, 'navbar.html')






#image search functionality
def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched any terms yet'
        return render(request, 'search.html',{"message": message})
