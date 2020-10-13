from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
# To change handle the dstination from here

def contact(request):
    return render(request, 'contact.html' )

def icons(request):
    return render(request, 'icons.html' )

def mens(request):
    return render(request, 'mens.html' )

def womens(request):
    return render(request, 'womens.html' )

def single(request):
    return render(request, 'single.html' )

def typography(request):
    return render(request, 'typography.html' )

