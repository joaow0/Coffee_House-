from django.contrib import admin


from django.contrib import admin
from .models import Products, Contacts, Testimonials, Gallery

admin.site.register(Products)
admin.site.register(Contacts)
admin.site.register(Testimonials)
admin.site.register(Gallery)