from django.contrib import admin

from medicine.models import *


class HospitalInline(admin.StackedInline):
    model = Hospital.doctors.through
    extra = 1


class DoctorInline(admin.StackedInline):
    model = Doctor.patients.through
    extra = 1


class DoctorAdmin(admin.ModelAdmin):
    filter_horizontal = ('patients',)
    inlines = (HospitalInline,)


class PatientAdmin(admin.ModelAdmin):
    inlines = (DoctorInline,)


admin.site.register(Hospital)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)

