from django.contrib import admin
from .models import Event, Muhurt
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile_no',
        'start_date',
        'end_date',
        'event_type'

    )


class MuhurtAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start_date',
        'end_date',

    )


admin.site.register(Event, EventAdmin)
admin.site.register(Muhurt, MuhurtAdmin)
