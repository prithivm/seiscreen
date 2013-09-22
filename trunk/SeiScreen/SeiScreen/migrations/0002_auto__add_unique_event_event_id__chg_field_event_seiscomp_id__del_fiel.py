# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Event', fields ['event_id']
        db.create_unique('seiscreen_event', ['event_id'])


        # Changing field 'Event.seiscomp_id'
        db.alter_column('seiscreen_event', 'seiscomp_id', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Deleting field 'SettingsChange.instutition'
        db.delete_column('seiscreen_settingschange', 'instutition')

        # Adding field 'SettingsChange.institution'
        db.add_column('seiscreen_settingschange', 'institution',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Event', fields ['event_id']
        db.delete_unique('seiscreen_event', ['event_id'])


        # Changing field 'Event.seiscomp_id'
        db.alter_column('seiscreen_event', 'seiscomp_id', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'SettingsChange.instutition'
        db.add_column('seiscreen_settingschange', 'instutition',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Deleting field 'SettingsChange.institution'
        db.delete_column('seiscreen_settingschange', 'institution')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seiscreen.client': {
            'Meta': {'object_name': 'Client'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'country_short': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'settings': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['seiscreen.Settings']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'seiscreen.event': {
            'Meta': {'object_name': 'Event'},
            '_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'id'"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'depth': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'event_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'magnitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'phase_count': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'relocation': ('django.db.models.fields.IntegerField', [], {}),
            'rms': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'seiscomp_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'time': ('django.db.models.fields.IntegerField', [], {})
        },
        'seiscreen.language': {
            'Meta': {'object_name': 'Language'},
            'admin_screen': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'automatic': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'back': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'browse': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'browse_events': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'change_pass': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'current_password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'custom_message': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'days': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'depth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'developed': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'event_filters': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'event_list': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'events_map': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'events_minimap': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'events_world': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalid_fields': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'latest': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'latest_global': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'latest_local': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'local_title_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'localonly': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'logout': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'mabove': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'magnitude': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'manual': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'map_zoom': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'minimap_zoom': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'new_password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'new_password_other': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'older': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password_changed': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'printlist': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'relevant': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'saveinfo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'screen_settings': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'seiscreen': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'seismicity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'settings_error': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sign_in': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'stations': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'today': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tools': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'try_again': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'week': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'world_title_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wrong_password': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'seiscreen.settings': {
            'Meta': {'object_name': 'Settings'},
            'bound_bottom': ('django.db.models.fields.IntegerField', [], {}),
            'bound_left': ('django.db.models.fields.IntegerField', [], {}),
            'bound_right': ('django.db.models.fields.IntegerField', [], {}),
            'bound_top': ('django.db.models.fields.IntegerField', [], {}),
            'center_lat': ('django.db.models.fields.IntegerField', [], {}),
            'center_lon': ('django.db.models.fields.IntegerField', [], {}),
            'custom_message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'events_map': ('django.db.models.fields.IntegerField', [], {}),
            'events_minimap': ('django.db.models.fields.IntegerField', [], {}),
            'events_world': ('django.db.models.fields.IntegerField', [], {}),
            'globe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'local_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'map_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'minimap_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'world_zoom': ('django.db.models.fields.IntegerField', [], {})
        },
        'seiscreen.settingschange': {
            'Meta': {'object_name': 'SettingsChange'},
            'bound_bottom': ('django.db.models.fields.IntegerField', [], {}),
            'bound_left': ('django.db.models.fields.IntegerField', [], {}),
            'bound_right': ('django.db.models.fields.IntegerField', [], {}),
            'bound_top': ('django.db.models.fields.IntegerField', [], {}),
            'center_lat': ('django.db.models.fields.IntegerField', [], {}),
            'center_lon': ('django.db.models.fields.IntegerField', [], {}),
            'custom_message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'events_map': ('django.db.models.fields.IntegerField', [], {}),
            'events_minimap': ('django.db.models.fields.IntegerField', [], {}),
            'events_world': ('django.db.models.fields.IntegerField', [], {}),
            'globe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostip': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'local_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'map_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'minimap_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'world_zoom': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['seiscreen']