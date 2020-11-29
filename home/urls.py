from django.contrib import admin
from django.urls import path
from .views import (

    event_calendar,
    search_event,
    login_view,
    logout_view

)
app_name = 'home'
urlpatterns = [
    path('', event_calendar, name='event_calendar'),
    path('search_event', search_event, name='search_event'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),

]
