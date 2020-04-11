from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreatenewForm
from .models import Event


class CreateNewView(LoginRequiredMixin, View):
    login_url = '/admin'

    def get(self, request, *args, **kwargs):
        form = CreatenewForm()
        context = {
            'form': form,

        }
        return render(request, 'create_new.html', context)

    def post(self, request, *args, **kwargs):
        form = CreatenewForm(request.POST or None)
        if request.method == 'POST':

            context = {
                'form': form
            }

            if form.is_valid():
                form.save()
                messages.success(
                    request, "New booking is created successfully.", extra_tags='alert-success')
                return render(request, 'create_new.html', context)

            else:
                print(form.errors)
                messages.error(
                    request, "Something went wrong. Try again", extra_tags='alert-danger')
        return render(request, 'create_new.html', context)


@login_required
@csrf_exempt
def check_all(request, *args, **kwargs):
    try:

        event = Event.objects.all()

        context = {
            'event': event,
            'total': Event.get_all_total()
        }
        return render(request, 'check_all.html', context)
    except ObjectDoesNotExist:
        messages.warning(request, "You do not have an event")
        return redirect('/')


@login_required
@csrf_exempt
def event_detail(request, slug):
    try:
        event = Event.objects.all().filter(slug=slug)
        context = {
            'event': event
        }
        return render(request, 'event_detail.html', context)
    except ObjectDoesNotExist:
        messages.error(request, "You do not have an event",
                       extra_tags='alert-danger')
        return redirect('bookings:check_all')


@login_required
@csrf_exempt
def update_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    form = CreatenewForm(request.POST or None, instance=event)
    if form.is_valid():
        event.save()
        messages.success(
            request, "Booking updated Successfully.", extra_tags='alert-success')
        return HttpResponseRedirect(event.get_absolute_url())
    context = {
        'event': event,
        'form': form
    }

    return render(request, 'update_event.html', context)


@login_required
def delete_event(request, slug):
    try:
        event = Event.objects.get(slug=slug)
        event.delete()
        messages.error(request, "Event Deleted Successfully",
                       extra_tags='alert-danger')
        return HttpResponseRedirect("/bookings/check_all")
    except ObjectDoesNotExist:
        messages.error(request, "Event Not found",
                       extra_tags='alert-danger')
        return HttpResponseRedirect("/bookings/check_all")
