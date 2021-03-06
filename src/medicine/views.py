# Create your views here.
import json
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse

from medicine.forms import PatientEditForm, DoctorForm
from medicine.models import Hospital, Doctor


@login_required
def index(request):
    """Index view to display hospitals, doctors and patients"""
    template = 'index.html'
    hospitals = Hospital.objects.all()
    return render_to_response(template, {'hospitals': hospitals}, context_instance=RequestContext(request))


@login_required
def edit_profile(request):
    """View to display form for editing patient-user profile and saving it"""

    template = 'edit_profile.html'
    if request.method == 'POST': # If the form has been submitted...
        form = PatientEditForm(request.POST, instance=request.user.patient) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect(reverse('index')) # Redirect after POST

    else:
        form = PatientEditForm(instance=request.user.patient)

    return TemplateResponse(request, template, {'form': form})


@login_required
def add_doctor(request):
    """View to create new doctor instance. Is to be displayed to staff and superuser only"""

    template = 'doctor_adding_form.html'
    #Check this in case url was typed directly in browser
    if request.user.is_staff and request.user.is_superuser:
        if request.method == "POST":
            form = DoctorForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                return TemplateResponse(request, template, {'form': form})
        else:
            form = DoctorForm()
            return TemplateResponse(request, template, {'form': form})
    return HttpResponseRedirect(reverse('index'))

@login_required
def ajax_patients_list(request, doctor_id):
    """Ajax view returns patients list template rendered for given doctor_id"""

    template = 'patients_list.html'
    if request.is_ajax():
        patients = Doctor.objects.get(pk=doctor_id).patients.all()
        return TemplateResponse(request, template, {'patients': patients})
    else:
        return HttpResponseRedirect(reverse('index'))
