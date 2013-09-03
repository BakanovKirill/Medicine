"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from medicine.models import *

class ModelsTest(TestCase):
    fixtures = ['initial.json', 'test_data.json']

    def setUp(self):
        self.doctors = Doctor.objects.all()
        self.hospitals = Hospital.objects.all()
        self.patients = Patient.objects.all()
        self.assertEqual(len(self.doctors), 3)
        self.assertEqual(len(self.patients), 2)
        self.assertEqual(len(self.hospitals), 2)

    def test_patients_doctors_hospitals(self):

        self.assertIn(Doctor.objects.filter(name="John")[0], self.patients[0].doctors.all())
        self.assertIn(Hospital.objects.get(pk=1), self.doctors[0].hospitals.all())
        self.assertNotIn(self.doctors[2], self.hospitals[0].doctors.all())

        new_one = Patient(name="Fill", surname="Bucket")
        new_one.save()
        new_one.doctors.add(self.doctors[1])

        self.assertEqual(1, new_one.doctors.all().count())

        new_doc = Doctor(name="Mac", surname="Murrey")
        new_doc.save()
        self.hospitals[1].doctors.add(new_doc)
        self.assertEqual(new_doc.name, self.hospitals[1].doctors.all()[3].name)


