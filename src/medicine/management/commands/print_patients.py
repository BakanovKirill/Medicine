### -*- coding: utf-8 -*- ####################################################

from django.core.management.base import BaseCommand
from django.db.models import F
from django.db.models.aggregates import Sum
from medicine.models import Patient

class Command(BaseCommand):
    '''Print to console all patients(__unicode__ value)'''
    args = ''
    help = 'Prints all patients from database to console'
    
    def handle(self, nodelete=False, *args, **options):
        print('Patients list:\n')
        for patient in Patient.objects.all():
            #Print patients
            print(patient)
