from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Event(models.Model):
    _id = models.IntegerField(primary_key=True, verbose_name='id', db_column='id')
    event_id = models.CharField(max_length=15, null=False, unique=True)
    seiscomp_id = models.CharField(max_length=50, null=False)
    time = models.IntegerField(null=False)
    country = models.CharField(max_length=15, null=False)
    region = models.CharField(max_length=30, null=False)
    latitude = models.DecimalField(decimal_places=3, max_digits=10)
    longitude = models.DecimalField(decimal_places=3, max_digits=10)
    magnitude = models.DecimalField(decimal_places=3, max_digits=10)
    depth = models.DecimalField(decimal_places=3, max_digits=10)
    phase_count = models.IntegerField(null=False)
    rms = models.DecimalField(decimal_places=3, max_digits=10)
    status = models.CharField(max_length=15, null=False)
    relocation = models.IntegerField(null=False)
    server = models.CharField(max_length=10, null=False)
    
    def __unicode__(self):
        return self.event_id


class Settings(models.Model):
    custom_message = models.CharField(max_length=140)
    language = models.CharField(max_length=3)
    globe = models.BooleanField()
    center_lat =  models.IntegerField()
    center_lon = models.IntegerField()
    bound_top = models.IntegerField()
    bound_bottom = models.IntegerField()
    bound_left = models.IntegerField()
    bound_right = models.IntegerField()
    world_zoom = models.IntegerField()
    local_zoom = models.IntegerField()
    events_map = models.IntegerField()
    events_minimap = models.IntegerField()
    events_world = models.IntegerField()
    map_zoom = models.IntegerField()
    minimap_zoom = models.IntegerField()
    
    def __unicode__(self):
		return "%s-%s" % (self.language, self.client.user)

    

class Client(models.Model):
    user = models.OneToOneField(User)
    settings = models.OneToOneField(Settings)
    country = models.CharField(max_length=15)
    country_short = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=lambda i, f: 'users/%s/%s' % (i.user.username, f))
    ip_address = models.CharField(max_length=16)
    
    def __unicode__(self):
        return "%s-%s" % (self.user, self.country)
    

class Language(models.Model):
    magnitude = models.CharField(max_length=15)
    lang = models.CharField(max_length=3)
    depth = models.CharField(max_length=15)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    location = models.CharField(max_length=20)
    stations = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    seiscreen = models.CharField(max_length=25)
    seismicity = models.CharField(max_length=25)
    latest = models.CharField(max_length=15)
    today = models.CharField(max_length=15)
    week = models.CharField(max_length=15)
    older = models.CharField(max_length=15)
    developed = models.CharField(max_length=15)
    latest_local = models.CharField(max_length=50)
    latest_global = models.CharField(max_length=50)
    automatic = models.CharField(max_length=20)
    manual = models.CharField(max_length=20)
    event_list = models.CharField(max_length=20)
    admin_screen = models.CharField(max_length=20)
    event_filters = models.CharField(max_length=20)
    mabove = models.CharField(max_length=20)
    localonly = models.CharField(max_length=20)
    days = models.CharField(max_length=20)
    browse = models.CharField(max_length=20)
    relevant = models.CharField(max_length=20)                      
    printlist = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sign_in = models.CharField(max_length=20)
    logout = models.CharField(max_length=20)
    back = models.CharField(max_length=20)
    map_zoom = models.CharField(max_length=20)
    minimap_zoom = models.CharField(max_length=20)
    events_map = models.CharField(max_length=150)
    events_minimap = models.CharField(max_length=20)
    events_world = models.CharField(max_length=20)
    custom_message = models.CharField(max_length=20)
    tools = models.CharField(max_length=20)
    screen_settings = models.CharField(max_length=20)
    change_pass = models.CharField(max_length=20)
    browse_events = models.CharField(max_length=20)
    saveinfo = models.CharField(max_length=20)
    wrong_password = models.CharField(max_length=20)
    password_changed = models.CharField(max_length=20)
    try_again = models.CharField(max_length=20)
    invalid_fields = models.CharField(max_length=20)
    settings_error = models.CharField(max_length=100)
    current_password = models.CharField(max_length=20)
    new_password = models.CharField(max_length=20)
    new_password_other = models.CharField(max_length=50)
    world_title_text = models.CharField(max_length=50)
    local_title_text = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.lang
        

class SettingsChange(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    hostip = models.CharField(max_length=16)
    custom_message = models.CharField(max_length=140)
    language = models.CharField(max_length=3)
    globe = models.BooleanField()
    center_lat =  models.IntegerField()
    center_lon = models.IntegerField()
    bound_top = models.IntegerField()
    bound_bottom = models.IntegerField()
    bound_left = models.IntegerField()
    bound_right = models.IntegerField()
    world_zoom = models.IntegerField()
    local_zoom = models.IntegerField()
    events_map = models.IntegerField()
    events_minimap = models.IntegerField()
    events_world = models.IntegerField()
    map_zoom = models.IntegerField()
    minimap_zoom = models.IntegerField()
    
    def __unicode__(self):
        return '%s-%s' % (self.date, self.user)
    

class Server(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


admin.site.register(Client)
admin.site.register(Settings)
admin.site.register(Language)
admin.site.register(Event)
admin.site.register(Server)
