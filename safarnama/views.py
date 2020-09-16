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
    dest1.offer=False

    dest2= Destination()
    dest2.name="UTTRAKHAND"
    dest2.desc="THe GateWay to heaven"
    dest2.price=8000
    dest2.img="destination_2.jpg"
    dest2.offer=False

    dest3= Destination()
    dest3.name="Delhi"
    dest3.desc="Capital"
    dest3.price=9000
    dest3.img="destination_3.jpg"
    dest3.offer=True

    dests=[dest1, dest2, dest3]
    
    return render(request, "index.html", {'dests': dests })
