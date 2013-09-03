from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=13)

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


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

