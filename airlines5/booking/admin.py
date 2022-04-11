from django.contrib import admin

from booking.models import Aircraft, Airport, Booking, Fly, Search

# Register your models here.
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Fly)
admin.site.register(Search)
admin.site.register(Booking)