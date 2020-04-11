from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify

S = 265000
G = 300000
PACKAGE_CHOICES = (
    (S, 'Silver'),
    (G, 'Gold')
)
EVENT_CHOICES = (
    ('Birth Day', 'Birth Day'),
    ('Marriage', 'Marriage'),
)


class Muhurt(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()


class Event(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    mobile_no = PhoneNumberField()
    address = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    package = models.IntegerField(choices=PACKAGE_CHOICES)
    cleaning_charges = models.IntegerField(blank=True, null=True, default=0)
    electricity_consumption = models.IntegerField(
        blank=True, null=True, default=0)
    property_damage_charges = models.IntegerField(
        blank=True, null=True, default=0)
    advance_paid = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name

    def total(self):
        return self.package + self.cleaning_charges + self.electricity_consumption + \
            self.property_damage_charges - self.advance_paid

    def get_absolute_url(self):
        return reverse("bookings:event_detail", kwargs={'slug': self.slug})

    def get_all_total():
        total = 0
        for event in Event.objects.all():
            total += event.total()
        return total


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Event.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_event_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_event_receiver, sender=Event)
