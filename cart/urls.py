from django.urls import path

from . import views

urlpatterns=[
    path("contact", views.contact, name="contact"),
    path("icons", views.icons, name="icons"),
    path("mens", views.mens, name="mens"),
    path("womens", views.womens, name="womens"),
    path("typography", views.typography, name="typography"),
    path("single", views.single, name="single")

]