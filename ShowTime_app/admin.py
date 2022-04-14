

from django.contrib import admin

# Register your models here.
from .models import Movies, Booking
admin.site.register(Movies)
admin.site.register(Booking)