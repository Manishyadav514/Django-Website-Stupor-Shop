from django.shortcuts import render
from .models import super

# Create your views here.
# To change handle the dstination from here
def index(request):
    dest1=super()
    dest1.name='Formal Blue shirt'
    dest1.price=200
    dest1.delete=400
    dest1.img='t1.jpg'
    dests=[dest1]

    dest2=super()
    dest2.name='Formal Blue shirt'
    dest2.price=300
    dest2.delete=400
    dest2.img='t1.jpg'
    
    dest3=super()
    dest3.name='Formal Blue shirt'
    dest3.price=300
    dest3.delete=400
    dest3.img='t1.jpg'
    dests=[dest1, dest2, dest3]

    return render(request, "index.html", {'dests':dests})
