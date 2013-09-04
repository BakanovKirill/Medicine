from django.contrib.auth.forms import UserChangeForm
from django.contrib import admin
from medicine.forms import PatientUserCreationForm

from medicine.models import *


class HospitalInline(admin.StackedInline):
    model = Hospital.doctors.through
    extra = 1


class DoctorInline(admin.StackedInline):
    model = Doctor.patients.through
    extra = 1


class PatientInline(admin.StackedInline):
    model = Patient
    extra = 1

class UserInline(admin.StackedInline):
    model = User
    extra = 1


class DoctorAdmin(admin.ModelAdmin):
    filter_horizontal = ('patients',)
    inlines = (HospitalInline,)


class HospitalAdmin(admin.ModelAdmin):
    filter_horizontal = ('doctors',)


class PatientAdmin(admin.ModelAdmin):
    inlines = (DoctorInline, )


class UserAdmin(admin.ModelAdmin):
    inlines = (PatientInline,)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.form = UserChangeForm
        return super(UserAdmin, self).change_view(request, object_id)

    def add_view(self, request, form_url='', extra_context=None):
        self.form = PatientUserCreationForm
        return super(UserAdmin, self).add_view(request)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)

