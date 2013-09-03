# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Doctor'
        db.create_table(u'medicine_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'medicine', ['Doctor'])

        # Adding M2M table for field patients on 'Doctor'
        db.create_table(u'medicine_doctor_patients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('doctor', models.ForeignKey(orm[u'medicine.doctor'], null=False)),
            ('patient', models.ForeignKey(orm[u'medicine.patient'], null=False))
        ))
        db.create_unique(u'medicine_doctor_patients', ['doctor_id', 'patient_id'])

        # Adding model 'Hospital'
        db.create_table(u'medicine_hospital', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'medicine', ['Hospital'])

        # Adding M2M table for field doctors on 'Hospital'
        db.create_table(u'medicine_hospital_doctors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hospital', models.ForeignKey(orm[u'medicine.hospital'], null=False)),
            ('doctor', models.ForeignKey(orm[u'medicine.doctor'], null=False))
        ))
        db.create_unique(u'medicine_hospital_doctors', ['hospital_id', 'doctor_id'])

        # Adding model 'Patient'
        db.create_table(u'medicine_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'medicine', ['Patient'])


    def backwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table(u'medicine_doctor')

        # Removing M2M table for field patients on 'Doctor'
        db.delete_table('medicine_doctor_patients')

        # Deleting model 'Hospital'
        db.delete_table(u'medicine_hospital')

        # Removing M2M table for field doctors on 'Hospital'
        db.delete_table('medicine_hospital_doctors')

        # Deleting model 'Patient'
        db.delete_table(u'medicine_patient')


    models = {
        u'medicine.doctor': {
            'Meta': {'object_name': 'Doctor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'patients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'doctors'", 'symmetrical': 'False', 'to': u"orm['medicine.Patient']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'medicine.hospital': {
            'Meta': {'object_name': 'Hospital'},
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'hospitals'", 'symmetrical': 'False', 'to': u"orm['medicine.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'medicine.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['medicine']