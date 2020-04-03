from django.contrib import admin
from .models import Event
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile_no',
        'start_date',
        'end_date',
        'event_type'

    )
    pass


admin.site.register(Event, EventAdmin)
