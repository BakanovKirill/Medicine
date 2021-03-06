"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.test import TestCase
from django.test.utils import override_settings

from medicine.models import *


class ModelsTest(TestCase):
    """Testing models present and loaded, test relations and proper values for some fields"""
    fixtures = ['initial.json', 'test_data.json']

    def setUp(self):
        self.doctors = Doctor.objects.all()
        self.hospitals = Hospital.objects.all()
        self.patients = Patient.objects.all()
        self.assertEqual(len(self.doctors), 3)
        self.assertEqual(len(self.patients), 4)
        self.assertEqual(len(self.hospitals), 2)

    def test_patients_doctors_hospitals(self):
        """test relations set correctly"""

        self.assertIn(Doctor.objects.filter(name="John")[0], self.patients[0].doctors.all())
        self.assertIn(Hospital.objects.get(pk=1), self.doctors[0].hospitals.all())
        self.assertNotIn(self.doctors[2], self.hospitals[0].doctors.all())

        new_one = Patient()

        new_one.user = User.objects.create(
            first_name='Phill', last_name='Phillips', username='phi', email='p@p.com')
        new_one.save()
        new_one.doctors.add(self.doctors[1])
        self.assertEqual(1, new_one.doctors.all().count())
        self.assertEqual('phi', Patient.objects.get(user__first_name='Phill').user.username)
        new_doc = Doctor(name="Mac", surname="Murrey")
        new_doc.save()
        self.hospitals[1].doctors.add(new_doc)
        self.assertEqual(new_doc.name, self.hospitals[1].doctors.all()[3].name)


class AuthTest(TestCase):
    """Test authentication and depending on authentication methods and views"""

    fixtures = ['initial.json', 'test_data.json']

    @override_settings(DEBUG=True)
    def test_login_required(self):
        #Check redirect for anonymous
        index_response = self.client.get(reverse('index'))
        profile_response = self.client.get(reverse('edit_profile'))
        self.assertEqual(302, index_response.status_code)
        self.assertEqual(302, profile_response.status_code)
        self.assertIn('login', index_response.items()[2][1])
        #Login and check index is visible now
        login_response = self.client.get(reverse('login'))
        self.assertContains(login_response, 'password')
        self.client.login(username='sun', password='admin')
        index_response = self.client.get(reverse('index'))
        self.assertContains(index_response, 'logout')
        self.assertContains(index_response, 'Sunny')
        #check doctors and hospitals present at index
        self.assertContains(index_response, 'John')
        self.assertContains(index_response, 'Garry')
        self.assertContains(index_response, 'Private Clinic')
        #Check profile edition is available
        profile_response = self.client.get(reverse('edit_profile'))
        self.assertContains(profile_response, 'email')
        self.assertContains(profile_response, 'submit')
        self.assertContains(profile_response, '380961665234')
        #Test that middleware worked and saved a lot of queries
        self.assertTrue(DatabaseQuery.objects.all().count() > 0)
        #check that settings is within context
        self.assertContains(index_response, 'medicine.wsgi.application')
        #check that template tag works ok
        self.assertContains(index_response, '<a href="/admin/medicine/hospital/1/">St. Savor</a>')


def test_profile_edit(self):
    """Test profile edit form responses"""

    self.client.login(username='sun', password='admin')
    profile_response = self.client.get(reverse('edit_profile'))
    self.assertEqual(200, profile_response.status_code)
    #Correct data
    response = self.client.post('/profiles/edit/',
                                {
                                    'first_name': 'asd',
                                    'last_name': 'fre',
                                    'email': 'asd@asd.com',
                                    'phone': '12356',
                                    'date_of_birth': '1991-02-01'
                                })
    #Redirect to index
    self.assertEqual(302, response.status_code)
    #Missing field data
    error_response = self.client.post('/profiles/edit/',
                                      {
                                          'first_name': 'asd',
                                          'last_name': 'fre',
                                          'email': 'asd@asd.com',
                                          'phone': '12356',
                                      })
    #Error displayed
    self.assertContains(error_response, 'This field is required')


class CommandTest(TestCase):
    """Test django management command. Or attempt to test it.."""

    fixtures = ['initial.json', 'test_data.json']

    def test_command(self):
        try:
            call_command('print_patients')
        except Exception:
            raise AssertionError('Command calling exception')