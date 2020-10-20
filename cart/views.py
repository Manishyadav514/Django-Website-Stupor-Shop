from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
# To change handle the dstination from here

def contact(request):
    return render(request, 'contact.html' )


def single(request):
    return render(request, 'single.html' )


