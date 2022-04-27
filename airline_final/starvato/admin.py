from django.contrib import admin

from .models import Identify, Airport, Aircraft, Fly, Booking, People

# Register your models here.
admin.site.register(Identify)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Fly)
admin.site.register(Booking)
admin.site.register(People)