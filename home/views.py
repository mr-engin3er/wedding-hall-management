from django.shortcuts import render, get_object_or_404
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from datetime import datetime
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from bookings.models import Event, Muhurt


@login_required
def event_calendar(request):
    muhurt = Muhurt.objects.all()
    event = Event.objects.all()
    context = {
        'event': event,
        'muhurt': muhurt
    }
    return render(request, 'index.html', context)


@login_required
def search_event(request):
    try:
        date = request.GET['date']
        date_event = Event.objects.all().filter(start_date=date)
    except:
        messages.error(request, "Event Not found for selected date ",
                       extra_tags='alert-danger')
        return HttpResponseRedirect("/")
    if date_event.exists():
        context = {
            'date_event': date_event
        }
        messages.error(request, "Event found for selected date ",
                       extra_tags='alert-success')
        return render(request, 'search_event.html', context)
    else:
        messages.error(request, "Event Not found for selected date ",
                       extra_tags='alert-danger')
        return HttpResponseRedirect("/")
