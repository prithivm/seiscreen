# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('seiscreen_event', (
            ('_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='id')),
            ('event_id', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('seiscomp_id', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('magnitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('depth', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('phase_count', self.gf('django.db.models.fields.IntegerField')()),
            ('rms', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('relocation', self.gf('django.db.models.fields.IntegerField')()),
            ('server', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('seiscreen', ['Event'])

        # Adding model 'Settings'
        db.create_table('seiscreen_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('custom_message', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('globe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('center_lat', self.gf('django.db.models.fields.IntegerField')()),
            ('center_lon', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_top', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_bottom', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_left', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_right', self.gf('django.db.models.fields.IntegerField')()),
            ('world_zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('local_zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('events_map', self.gf('django.db.models.fields.IntegerField')()),
            ('events_minimap', self.gf('django.db.models.fields.IntegerField')()),
            ('events_world', self.gf('django.db.models.fields.IntegerField')()),
            ('map_zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('minimap_zoom', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('seiscreen', ['Settings'])

        # Adding model 'Client'
        db.create_table('seiscreen_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('settings', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['seiscreen.Settings'], unique=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('country_short', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('seiscreen', ['Client'])

        # Adding model 'Language'
        db.create_table('seiscreen_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('magnitude', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('depth', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('stations', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('seiscreen', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('seismicity', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('latest', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('today', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('week', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('older', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('developed', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('latest_local', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('latest_global', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('automatic', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('manual', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('event_list', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('admin_screen', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('event_filters', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mabove', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('localonly', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('days', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('browse', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('relevant', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('printlist', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sign_in', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('logout', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('back', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('map_zoom', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('minimap_zoom', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('events_map', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('events_minimap', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('events_world', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('custom_message', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tools', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('screen_settings', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('change_pass', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('browse_events', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('saveinfo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('wrong_password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password_changed', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('try_again', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('invalid_fields', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('settings_error', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('current_password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('new_password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('new_password_other', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('world_title_text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('local_title_text', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('seiscreen', ['Language'])

        # Adding model 'SettingsChange'
        db.create_table('seiscreen_settingschange', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('instutition', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('hostip', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('custom_message', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('globe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('center_lat', self.gf('django.db.models.fields.IntegerField')()),
            ('center_lon', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_top', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_bottom', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_left', self.gf('django.db.models.fields.IntegerField')()),
            ('bound_right', self.gf('django.db.models.fields.IntegerField')()),
            ('world_zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('local_zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('events_map', self.gf('django.db.models.fields.IntegerField')()),
            ('events_minimap', self.gf('django.db.models.fields.IntegerField')()),
            ('events_world', self.gf('django.db.models.fields.IntegerField')()),
            ('map_zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('minimap_zoom', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('seiscreen', ['SettingsChange'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('seiscreen_event')

        # Deleting model 'Settings'
        db.delete_table('seiscreen_settings')

        # Deleting model 'Client'
        db.delete_table('seiscreen_client')

        # Deleting model 'Language'
        db.delete_table('seiscreen_language')

        # Deleting model 'SettingsChange'
        db.delete_table('seiscreen_settingschange')


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
            'event_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'magnitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'phase_count': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'relocation': ('django.db.models.fields.IntegerField', [], {}),
            'rms': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'seiscomp_id': ('django.db.models.fields.IntegerField', [], {}),
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
            'instutition': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'local_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'map_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'minimap_zoom': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'world_zoom': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['seiscreen']