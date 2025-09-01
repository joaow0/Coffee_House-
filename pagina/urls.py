from .views import header
from django.urls import path

urlpatterns = [
    path('', header.home, name='home'),
    path('about/', header.about, name='about'),
    path('menu/', header.menu, name='menu'),
    path('testimonials/', header.testimonials, name='testimonials'),
    path('gallery/', header.gallery, name='gallery'),
    path('contacts/', header.contacts, name='contacts'),
]
