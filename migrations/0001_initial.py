# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CurrUser'
        db.create_table(u'getuser_curruser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curr_user', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'getuser', ['CurrUser'])


    def backwards(self, orm):
        # Deleting model 'CurrUser'
        db.delete_table(u'getuser_curruser')


    models = {
        u'getuser.curruser': {
            'Meta': {'object_name': 'CurrUser'},
            'curr_user': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['getuser']