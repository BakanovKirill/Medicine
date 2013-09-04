from django.db.models import signals
from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    user = models.OneToOneField(User, null=True, parent_link=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=13)

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patients = models.ManyToManyField(Patient, related_name='doctors', blank=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class Hospital(models.Model):
    title = models.CharField(max_length=255)
    doctors = models.ManyToManyField(Doctor, related_name='hospitals', blank=True)

    def __unicode__(self):
        return '%s' % self.title


class DatabaseQuery(models.Model):
    query = models.TextField(blank=True)


def patient_save_signal(sender, instance, created, raw, update_fields, **kwargs):
    signals.post_save.disconnect(patient_save_signal, sender=Patient)
    instance.save()
    signals.post_save.connect(patient_save_signal, sender=Patient)

signals.post_save.connect(patient_save_signal, sender=Patient)