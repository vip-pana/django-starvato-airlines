from django.contrib import admin
from .models import Airport, Search, Fly, Aircraft, Booking

admin.site.register(Airport)
admin.site.register(Search)
admin.site.register(Fly)
admin.site.register(Aircraft)
admin.site.register(Booking)