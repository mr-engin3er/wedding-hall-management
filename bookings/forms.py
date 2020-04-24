from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Event


class CreatenewForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'name',
            'mobile_no',
            'address',
            'start_date',
            'end_date',
            'event_type',
            'package',
            'cleaning_charges',
            'electricity_consumption',
            'property_damage_charges',
            'advance_paid',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['start_date'].input_formats = settings.DATE_INPUT_FORMATS
        # self.fields['end_date'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['name'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'name', 'plceholder': 'Enter name'})
        self.fields['mobile_no'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'mobile_no', 'data-prefix': '+91'})
        self.fields['address'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'inputAddress', 'placeholder': '1234 Main St'})
        self.fields['start_date'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'picker-1'})
        self.fields['end_date'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'picker-2'})
        self.fields['event_type'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'name'})
        self.fields['package'].widget.attrs.update(
            {'type': 'number', 'class': 'form-control', 'id': 'package'})
        self.fields['cleaning_charges'].widget.attrs.update(
            {'type': 'number', 'class': 'form-control', 'id': 'cleaning_charges'})
        self.fields['electricity_consumption'].widget.attrs.update(
            {'type': 'number', 'class': 'form-control', 'id': 'electricity_consumption'})
        self.fields['property_damage_charges'].widget.attrs.update(
            {'type': 'number', 'class': 'form-control', 'id': 'property_damage_charges'})
        self.fields['advance_paid'].widget.attrs.update(
            {'type': 'number', 'class': 'form-control', 'id': 'advance_paid'})
