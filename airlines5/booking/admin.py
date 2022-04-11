from django.contrib import admin

from booking.models import Aircraft, Airport, Fly

# Register your models here.
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Fly)