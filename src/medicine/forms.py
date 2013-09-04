from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelMultipleChoiceField
from django.utils.translation import ugettext_lazy as _
from django import forms

from medicine.widgets import *
from medicine.models import Patient, Doctor, Hospital


class PatientEditForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(label=_('Contact email:'), required=True)
    phone = forms.CharField(help_text=_('Example: 380961112233'), required=False)
    date_of_birth = forms.DateField(widget=CalendarWidget)

    def __init__(self, *args, **kwargs):
        super(PatientEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email
        self.fields.keyOrder = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth'
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if len(phone) > 12:
            raise forms.ValidationError('Phone number length is incorrect!')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user != self.instance.user:
                raise forms.ValidationError("Email is already taken by another user!")
        except ObjectDoesNotExist:
            pass
        return email

    def save(self, *args, **kwargs):
        super(PatientEditForm, self).save(*args, **kwargs)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.email = self.cleaned_data.get('email')
        self.instance.user.save()

    class Meta:
        model = Patient


class PatientUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'username']

    def __init__(self, *args, **kwargs):
        super(PatientUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields.keyOrder = [
            'email',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'surname', 'patients',)

    hospitals = ModelMultipleChoiceField(
        queryset=Hospital.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('hospitals', False),
        )

    def save(self, *args, **kwargs):
        super(DoctorForm, self).save(*args, **kwargs)
        for hospital in self.cleaned_data.get('hospitals'):
            hospital.doctors.add(self.instance)