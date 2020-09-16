from django.shortcuts import render
from .models import Destination

# Create your views here.
# To change handle the dstination from here
def index(request):
    dest1= Destination()
    dest1.name="GOA"
    dest1.desc="The city of fun"
    dest1.price=7000
    dest1.img="destination_1.jpg"
    
    return render(request, "index.html", {'dest1': dest1 })
