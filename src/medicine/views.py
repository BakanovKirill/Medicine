# Create your views here.
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse

from medicine.forms import PatientEditForm

@login_required
def index(request):
    template = 'index.html'
    return render_to_response(template, {}, context_instance=RequestContext(request))

@login_required
def edit_profile(request):
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
