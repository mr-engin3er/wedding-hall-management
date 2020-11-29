from django.shortcuts import render, get_object_or_404, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from datetime import datetime
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from bookings.models import Event, Muhurt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}",extra_tags='alert-success')
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.",extra_tags='alert-danger')
        else:
            messages.error(request, "Invalid username or password.",extra_tags='alert-danger')
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!",extra_tags='alert-secondary')
    return redirect("/login")

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
