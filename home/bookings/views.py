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
    slug = request.POST.get('slug', '')
    type = request.POST.get('type', '')
    value = request.POST.get('value', '')
    event = Event.objects.get(slug=slug)

    if type == "name":
        event.name = value

    if type == "mobile_no":
        event.mobile_no = value

    if type == "start_date":
        event.start_date = value

    if type == "end_date":
        event.end_date = value

    if type == "event_type":
        event.event_type = value

    if type == "address":
        event.address = value

    if type == "package":
        event.package = value

    if type == "advance_paid":
        event.advance_paid = value

    if type == "cleaning_charges":
        event.cleaning_charges = value

    if type == "electricity_consumption":
        event.electricity_consumption = value

    if type == "property_damage_charges":
        event.property_damage_charges = value

    event.save()
    return JsonResponse({"success": "Updated successfully"})


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
