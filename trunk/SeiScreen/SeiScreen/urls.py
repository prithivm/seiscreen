from django.conf.urls import patterns, include, url
from django.contrib import admin

from seiscreen.views import data_update, reset_password, screen, your_ip, \
                    get_audio, admin_screen, event_list, fetch_events, admin_login, admin_logout, \
                    admin_save, admin_password, change_password, latest_events

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SeiScreen.views.home', name='home'),
    # url(r'^SeiScreen/', include('SeiScreen.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/$', data_update),
    url(r'^reset/$', reset_password),
    
    url(r'^screen/$', screen),
    url(r'^seiscreen/screen/$', screen),
    
    url(r'^seiscreen/update/$', data_update),
    url(r'^my-ip/$', your_ip),
    url(r'^audio/(\d+).mp3', get_audio),
    url(r'^seiscreen/audio/(\d+).mp3', get_audio),
    
    url(r'^seiscreen/admin-screen/$', admin_screen),
    url(r'^admin-screen/$', admin_screen),
    url(r'^seiscreen/admin-screen/$', admin_screen),
    url(r'^admin-save/$', admin_save),
    url(r'^seiscreen/admin-save/$', admin_save),
    url(r'^seiscreen/event-list/$', event_list),
    url(r'^event-list/$', event_list),
    url(r'^fetch-events/(\d+)/(\d+)/(\w+)/(-?\d+)/(\w+)/$', fetch_events),
    url(r'^seiscreen/fetch-events/(\d+)/(\d+)/(\w+)/(-?\d+)/(\w+)/$', fetch_events),
    
    url(r'^fetch-events/(\d+)/(\d+)/(\w+)/(-?\d+)/$', fetch_events),
    url(r'^seiscreen/fetch-events/(\d+)/(\d+)/(\w+)/(-?\d+)/$', fetch_events),
    
    url(r'^$', admin_login),
    
    url(r'^login/$', admin_login),
    url(r'^logout/$', admin_logout),
    url(r'^seiscreen/login/$', admin_login),
    url(r'^seiscreen/logout/$', admin_logout),
    
    url(r'^seiscreen/admin-password/$', admin_password),
    url(r'^admin-password/$', admin_password),
    
    url(r'^seiscreen/change-password/$', change_password),
    url(r'^change-password/$', change_password),
    
    url(r'^seiscreen/latest-events/$', latest_events),
    url(r'^latest-events/$', latest_events),
)