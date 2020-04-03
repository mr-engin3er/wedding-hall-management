from django.contrib import admin
from django.urls import path
from .views import (
    CreateNewView,
    check_all,
    event_detail,
    update_event,
    delete_event
)
app_name = 'bookings'
urlpatterns = [
    path('create_new', CreateNewView.as_view(), name='create_new'),
    path('check_all', check_all, name='check_all'),
    path('event_detail/<slug>', event_detail, name='event_detail'),
    path('update_event/<slug>', update_event, name='update_event'),
    path('delete_event/<slug>', delete_event, name='delete_event'),

]
