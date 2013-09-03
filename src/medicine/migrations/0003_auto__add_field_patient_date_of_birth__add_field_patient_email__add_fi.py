# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Patient.date_of_birth'
        db.add_column(u'medicine_patient', 'date_of_birth',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Patient.email'
        db.add_column(u'medicine_patient', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Patient.phone'
        db.add_column(u'medicine_patient', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=13, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Patient.date_of_birth'
        db.delete_column(u'medicine_patient', 'date_of_birth')

        # Deleting field 'Patient.email'
        db.delete_column(u'medicine_patient', 'email')

        # Deleting field 'Patient.phone'
        db.delete_column(u'medicine_patient', 'phone')


    models = {
        u'medicine.doctor': {
            'Meta': {'object_name': 'Doctor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'patients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'doctors'", 'blank': 'True', 'to': u"orm['medicine.Patient']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'medicine.hospital': {
            'Meta': {'object_name': 'Hospital'},
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'hospitals'", 'blank': 'True', 'to': u"orm['medicine.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'medicine.patient': {
            'Meta': {'object_name': 'Patient'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['medicine']