from django.shortcuts import render
from .models import super

# Create your views here.
# To change handle the dstination from here
def index(request):
    dest1=super()
    dest1.name='?'
    dest1.price=200
    dest1.delete=400
    dest1.img='t1.jpg'
    dests=[dest1]
    
    return render(request, "index.html", {'dests':dests})
