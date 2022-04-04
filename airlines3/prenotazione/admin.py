from django.contrib import admin

from.models import Airport, Fly, SearchFly
# Register your models here.

admin.site.register(Airport)
admin.site.register(Fly)
admin.site.register(SearchFly)