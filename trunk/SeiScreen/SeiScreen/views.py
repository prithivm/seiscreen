# -*- coding: latin-1 -*-

import os
import json
import datetime

#import cStringIO as StringIO
#from cgi import escape

from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404
from django.template.loader import get_template
from django.template import Context

#import ho.pisa as pisa

try:
    import SeiScreen.settings as settings
except ImportError:
    import settings

import models
import flengp as spanish_regions

SECS_DAY = 86400
SECS_WEEK = 604800
SECS_MONTH = 2629400

VOICE_COMMAND = '''echo "%s" | text2wave -scale 1 -F 44000 -o %s %s;
                   lame %s %s'''
                   
VOICE_SPA_SELECTOR = '-eval "(voice_JuntaDeAndalucia_es_pa_diphone)"'
VOICE_ENG_SELECTOR = '-eval "(voice_kal_diphone)"'

def your_ip(request):
    return HttpResponse('{"ip": "%s"}' % request.META['REMOTE_ADDR'], content_type='application/json') 

def data_update(request):
    response = {}
    context = RequestContext(request)
    client = _get_client(request)
    
    client_lang = client.settings.language
    lang = _make_lang_dict(client_lang)
    
    # Gets the time of the oldest event to show.
    settime = _unix_now() - client.settings.events_map * (SECS_DAY)
    all_events = models.Event.objects.filter(time__gte=settime).order_by('-time')[:2000]
    eventsminimap = client.settings.events_minimap
    
    current_server = all_events[0].server
    local_events = []
    local_countries = client.country_short.split(',')
    
    # Find the most recent global event that is not from clients country(s).
    first_global = False
    for event in all_events:
        if event.country not in local_countries and not first_global:
            latest_global = event
            first_global = True
            
        elif event.country in local_countries and len(local_events) < 100:
            local_events.append(event)
            
    all_events = all_events[:100]
            
    center_lat = client.settings.center_lat
    center_lon = client.settings.center_lon
    bound_t = client.settings.bound_top
    bound_b = client.settings.bound_bottom
    bound_r = client.settings.bound_right
    bound_l = client.settings.bound_left
    world_zoom = client.settings.world_zoom
    local_zoom = client.settings.local_zoom
    
    latest_local = local_events[0]
    lastchange = models.SettingsChange.objects.filter(user=client.user.username).order_by('-date')[0]

    response['servers'] = _servers_to_dict()
    response['latest_global'] = _event_to_dict(latest_global, lang)
    response['latest_local'] = _event_to_dict(latest_local, lang)
    response['global_event_list'] = _make_list(all_events, lang)
    response['local_event_list'] = _make_list(local_events, lang)
    response['latest_local_list'] = _make_local_list(local_events[:eventsminimap], lang)
    response['connection_status'] = {'status':1}
    response['server'] = current_server
    response['events'] = {'count':0}
    response['global_positioning'] = {'center_lat':center_lat, 'center_lon':center_lon, 
                    'bound_l':bound_l, 'bound_b':bound_b, 'bound_r':bound_r, 'bound_t':bound_t,
                    'zoom_mainmap':world_zoom, 'zoom_minimap':local_zoom}
   
    response['settings_change'] = lastchange.date
    
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')

def _time_from_unix(unix_time):
        tdiff = _unix_now() - unix_time
        
        if tdiff <= SECS_DAY:
            return 2
            
        elif (tdiff > SECS_DAY) and (tdiff <= SECS_WEEK):
            return 3
            
        elif (tdiff > SECS_WEEK):
            return 4


def _servers_to_dict():
    servers = [] 
    ss = models.Server.objects.all()

    for s in ss:
        servers.append(dict(
            name=s.name, address=s.address))

    return servers


def _event_to_dict(event, lang, latest = False):
    event_dict = {}
    
    event_dict['mag'] = event.magnitude
    event_dict['lat'] = event.latitude
    event_dict['lon'] = event.longitude
    event_dict['depth'] = event.depth
    event_dict['time'] = event.time
    event_dict['country'] = event.country
    event_dict['stations'] = event.phase_count
    event_dict['id'] = event.pk
    event_dict['status'] = lang[event.status]
    event_dict['region'] = _get_region(event, lang['lang'])
    
    if latest:
        event_dict['color'] = _time_from_unix(event.time)
        
    else:
        event_dict['color'] = 1
    
    return event_dict

def _make_list(events, lang):
    event_list = []
    
    for event in events:
        event_dict = {}
        event_dict['mag'] = event.magnitude
        event_dict['lat'] = event.latitude
        event_dict['lon'] = event.longitude
        event_dict['id'] = event.pk
        event_dict['color'] = _time_from_unix(event.time)
        event_dict['time'] = event.time
        event_dict['country'] = _get_region(event, lang['lang'])

        event_list.append(event_dict)
        
    event_list[0]['color'] = 1
    
    return event_list

def _make_local_list(events, lang):
    event_list = []
    
    for i in range(0, len(events)):
        try:
            event_dict = {}
            event_dict['region'] = _get_region(events[i], lang['lang'])
            event_dict['id'] = events[i].pk
            event_dict['time'] = events[i].time
            event_dict['mag'] = events[i].magnitude
            event_dict['lat'] = events[i].latitude
            event_dict['lon'] = events[i].longitude
            
            if len(event_dict['region']) >= 40:
                event_dict['region'] = event_dict['region'][:40]
                event_dict['region'] += '...'
                
            event_list.append(event_dict)
        
        except IndexError:
            break;
        
    return event_list

def _get_region(event, lang, correct_accents=True):
    if lang == 'esp':
        region = spanish_regions.FlEngLookup(event.latitude, event.longitude)[0]
        
        if correct_accents:
            region = _correct_accent(region)
        
    else:
        region = event.region
    
    return region

def _correct_accent(phrase, lan='esp'):
    if lan == 'esp':
        phrase = phrase.replace("'a", "á")
        phrase = phrase.replace("'e", "é")
        phrase = phrase.replace("'i", "í")
        phrase = phrase.replace("'o", "ó")
        phrase = phrase.replace("'u", "ú")
    
    return phrase

def _total_seconds(td):
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    
def _unix_time(time):
    return _total_seconds(time - datetime.datetime(1970, 1, 1, 0, 0, 0))
    
def _unix_now():
    return _unix_time(datetime.datetime.utcnow())

def reset_password(request):
    admin = User.objects.all()[0]
    admin.set_password('lopikljH;')
    admin.save()
    
    return HttpResponse('Changed...')

def screen(request):
    context = RequestContext(request)
    client = _get_client(request)
    
    lang = _make_lang_dict(client.settings.language)
    
    context['custom_text'] = client.settings.custom_message
    context['globe'] = client.settings.globe
    context['language'] = lang
    context['screen_title'] = '%s: %s %s' % (lang['seiscreen'], lang['seismicity'], client.country)
    context['country'] = client.country
    context['institution'] = client.institution
    context['older_events'] = str(client.settings.events_map) + ' ' + lang['days']
    
    return render_to_response('screen.html', context)
    
def _get_client(request):
    # Super user can see the screen from any IP.
    if request.user.is_superuser:
       return get_object_or_404(models.Client, user=request.user)
    
    else:
        client_ip = request.META['REMOTE_ADDR']
        return get_object_or_404(models.Client, ip_address=client_ip)
    
def _make_lang_dict(lang):
    language = _get_lang(lang)

    langdict = {}
    langdict['lang'] = language.lang
    langdict['depth'] = language.depth
    langdict['latitude'] = language.latitude
    langdict['longitude'] = language.longitude
    langdict['stations'] = language.stations
    langdict['location'] = language.location
    langdict['status'] = language.status
    langdict['time'] = language.time
    langdict['seiscreen'] = language.seiscreen
    langdict['seismicity'] = language.seismicity
    langdict['latest'] = language.latest
    langdict['today'] = language.today
    langdict['week'] = language.week
    langdict['older'] = language.older
    langdict['developed'] = language.developed
    langdict['magnitude'] = language.magnitude
    langdict['latest_local'] = language.latest_local
    langdict['latest_global'] = language.latest_global
    langdict['mag'] = language.magnitude[0].capitalize()
    langdict['depthshort'] = language.depth[0].capitalize()
    langdict['latshort'] = language.latitude[:3].capitalize()
    langdict['lonshort'] = language.longitude[:3].capitalize()
    langdict['automatic'] = language.automatic
    langdict['manual'] = language.manual
    langdict['event_list'] = language.event_list
    langdict['admin_screen'] = language.admin_screen
    langdict['event_filters'] = language.event_filters
    langdict['mabove'] = language.mabove
    langdict['localonly'] = language.localonly
    langdict['days'] = language.days
    langdict['browse'] = language.browse
    langdict['relevant'] = language.relevant
    langdict['printlist'] = language.printlist
    langdict['date'] = language.date
    langdict['login'] = language.login
    langdict['username'] = language.username
    langdict['password'] = language.password
    langdict['sign_in'] = language.sign_in
    langdict['logout'] = language.logout
    langdict['back'] = language.back
    langdict['map_zoom'] = language.map_zoom
    langdict['minimap_zoom'] = language.minimap_zoom
    langdict['events_map'] = language.events_map
    langdict['events_minimap'] = language.events_minimap
    langdict['events_world'] = language.events_world
    langdict['custom_message'] = language.custom_message
    langdict['tools'] = language.tools
    langdict['screen_settings'] = language.screen_settings
    langdict['change_pass'] = language.change_pass
    langdict['browse_events'] = language.browse_events
    langdict['save'] = language.saveinfo
    langdict['wrong_password'] = language.wrong_password
    langdict['password_changed'] = language.password_changed
    langdict['try_again'] = language.try_again
    langdict['invalid_fields'] = language.invalid_fields
    langdict['current_password'] = language.current_password
    langdict['new_password'] = language.new_password
    langdict['settings_error'] = language.settings_error
    langdict['new_password_other'] = language.new_password_other
    langdict['local_title_text'] = language.local_title_text
    langdict['world_title_text'] = language.world_title_text
    
    return langdict 

def _get_lang(lang):
    try:
        language = models.Language.objects.get(lang=lang)
        
    except:
        language = models.Language.objects.get(lang='eng')
        
    return language
    
def get_audio(request, eid):
    client = _get_client(request)
    eid = int(eid)
    lan = str(client.settings.language)
    file_path = '%s/media/audio/%d-%s.%s'
    mp3_path = file_path % (settings.PROJECT_PATH, eid, lan, 'mp3')
    wav_path = file_path % (settings.PROJECT_PATH, eid, lan, 'wav')
    
    # Should not announce events older than 1 hour.
    event = get_object_or_404(models.Event, pk=eid)
    
    if _unix_now() - event.time > 3600:
        raise Http404
    
    try:
        audio_file = open(mp3_path, 'rb')
        
    # Create audio file.
    except IOError:        
        message = ''
        region = region = _get_region(event, lan, False)
        voice = ''
        decimal_separator = ''
        if lan == 'esp':
            message += '''Sismo, en %s, de magnitud %.1f,
                           y profundidad %d kil'ometros'''
            
            voice = VOICE_SPA_SELECTOR
            decimal_separator = 'punto'
            
        elif lan == 'eng':
            message += '''earthquake, in %s, magnitude %.1f,
                          and depth %d kilometers'''
            
            voice = VOICE_ENG_SELECTOR
            decimal_separator = 'point'
            
        message = message % (region, event.magnitude, event.depth)
        message = message.replace('.', ' %s ' % decimal_separator)
        create_command = VOICE_COMMAND % (message, wav_path, voice, wav_path, mp3_path)
        os.system(create_command)
        
        try:
            audio_file = open(mp3_path, 'rb')
        
        except:
            raise Http404
    
    response = HttpResponse(audio_file, mimetype='audio/mp3')
    response['Content-Disposition'] = 'attachment; filename=%s' % mp3_path.split('/')[-1]
    return response

def admin_login(request):
    requestlang = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0]
    context = RequestContext(request)
    
    if request.method == 'POST':
        posted = request.POST

        usrname = posted.get('usrname', None)
        passwd = posted.get('passwd', None)
        
        user = authenticate(username=usrname, password=passwd)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', '')
            
            if not next_url or next_url == '/':
                next_url = '/admin-screen/'
            
            return HttpResponseRedirect('/seiscreen' + next_url)
    
    if requestlang.startswith('es'):
        language = _make_lang_dict('esp')
        
    else:
        language = _make_lang_dict('eng')
    
    context['next'] = request.GET.get('next', '')
    context['language'] = language
    
    return render_to_response('admin_login.html', context)

@login_required(None, 'next', '/login/')
def admin_screen(request):
    client = models.Client.objects.get(user=request.user)
    context = RequestContext(request)
    context['language'] = _make_lang_dict(client.settings.language)
    context['page_title'] = context['language']['admin_screen']
    context['institution'] = client.institution
    context['settings'] = client.settings
    context['admin'] = request.user.is_superuser
    
    return render_to_response('admin_screen.html', context)

@login_required
def admin_save(request):
    context = RequestContext(request)
    try:
        client = get_object_or_404(models.Client, user=request.user)
        settings = client.settings
        context['errors'] = True
        if request.method == 'POST':
            events_map = int(request.POST.get('events_map', 0))
            minimap_zoom = int(request.POST.get('minimap_zoom', 0))
            events_minimap = int(request.POST.get('events_minimap', 0))
            custom_message = request.POST.get('custom_message', '')
            
            if not events_map or not events_minimap or \
               not minimap_zoom or not custom_message:

                raise Exception
            
            else:
                settingslog = models.SettingsChange(user=client.user.username,
                                      institution=client.institution,
                                      hostip=request.META['REMOTE_ADDR'],
                                      custom_message=custom_message,
                                      language=client.settings.language,
                                      globe=client.settings.globe,
                                      center_lat=client.settings.center_lat,
                                      center_lon=client.settings.center_lon,
                                      bound_top=client.settings.bound_top,
                                      bound_bottom=client.settings.bound_bottom,
                                      bound_left=client.settings.bound_left,
                                      bound_right=client.settings.bound_bottom,
                                      world_zoom=client.settings.world_zoom,
                                      local_zoom=client.settings.local_zoom,
                                      events_map=events_map,
                                      events_minimap=events_minimap,
                                      events_world=client.settings.events_world,
                                      map_zoom=client.settings.map_zoom,
                                      minimap_zoom=minimap_zoom)
                
                context['errors'] = False
            	settings.events_map = events_map
            	settings.events_minimap = events_minimap
                settings.minimap_zoom = minimap_zoom
                settings.custom_message = custom_message
                
                settings.save(force_update=True)
                settingslog.save(force_insert=True)
                                          
    finally:
        context['settings'] = settings
        context['language'] = _make_lang_dict(settings.language)
        context['page_title'] = context['language']['admin_screen']
        context['institution'] = client.institution
        
        return render_to_response('admin_screen.html', context)

@login_required(None, 'next', '/login/')
def event_list(request):
    client = models.Client.objects.get(user=request.user)
    context = RequestContext(request)
    context['language'] = _make_lang_dict(client.settings.language)
    context['page_title'] = context['language']['event_list']
    context['institution'] = client.institution
    
    return render_to_response('admin_list.html', context)
    
@login_required(None, 'next', '/login/')
def fetch_events(request, m_thresh, days, localonly, limit, topdf = 'false'):
    if request.is_ajax() or topdf == 'true':
        m_thresh = int(m_thresh)
        days = int(days)
        localonly = str(localonly)
        limit = int(limit)
        topdf = str(topdf)
        
        if limit < 0:
            limit = 2000
        
        context = RequestContext(request)
        query_events = []
        client = models.Client.objects.get(user=request.user)
        local_countries = client.country_short.split(',')
        all_events = models.Event.objects.order_by('-time')[:limit]
        t_thresh = _unix_now() - (days * SECS_DAY)
        
        if localonly == 'true':
            localonly = True
        
        else:
            localonly = False
            
        if topdf == 'true':
            topdf = True
            
        else:
            topdf = False
        
        major_event = {}
        for event in all_events:
            if event.time >= t_thresh and event.magnitude >= m_thresh:
                if event.country in local_countries or not localonly:
                    eventdict = {}
                    eventdict['magnitude'] = '%.1f' % event.magnitude
                    eventdict['longitude'] = '%.2f' % event.longitude
                    eventdict['latitude'] = '%.2f' % event.latitude
                    eventdict['rms'] = '%.1f' % event.rms
                    eventdict['region'] = _get_region(event, client.settings.language)
                    eventdict['date'] =  str(datetime.datetime.fromtimestamp(event.time))
                    eventdict['depth'] = '%d' % event.depth
                    eventdict['stations'] = event.phase_count
                    
                    if len(query_events) == 0 or \
                       float(major_event.get('magnitude', '0.0')) < float(eventdict.get('magnitude', '0.0')):
                        major_event = eventdict

                    query_events.append(eventdict)

        if len(query_events) == 0:
            return HttpResponse('')
        
        else:
            major_event['region'] = major_event['region'][:40]
            context['relevant'] = major_event
            context['queried'] = query_events
            context['language'] = _make_lang_dict(client.settings.language)
            
            if topdf:
                context['date'] = str(datetime.datetime.fromtimestamp(_unix_now()))
                template = get_template('pdf_events.html')
                html  = template.render(context)
                result = StringIO.StringIO()

                pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-16")), result)
                
                if not pdf.err:
                    return HttpResponse(result.getvalue(), mimetype='application/pdf')
        
                return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
                
            else:
                return render_to_response('fetched.html', context)
    
    else:
        return HttpResponse('')

@login_required
def latest_events(request):
    client = get_object_or_404(models.Client, user=request.user)
    context = RequestContext(request)
    context['language'] = _make_lang_dict(client.settings.language)
    context['page_title'] = context['language']['event_list']
    context['institution'] = client.institution
    
    return render_to_response('perm_list.html', context)
    
@login_required
def admin_password(request):
    client = get_object_or_404(models.Client, user=request.user)
    context = RequestContext(request)
    context['language'] = _make_lang_dict(client.settings.language)
    
    return render_to_response('change_pass.html', context)

@login_required
def change_password(request):
    if request.is_ajax() and request.method == 'POST':
        response = {}
        password = request.POST.get('password', '')
        newpassword = request.POST.get('new_password', '')
        
        client = get_object_or_404(models.Client, user=request.user)
        language = _get_lang(client.settings.language)
        
        if not password or not newpassword:
            response['success'] = 'false'
            response['error_message'] = language.invalid_fields
                        
        else:
            if not request.user.check_password(password):
                response['success'] = 'false'
                response['error_message'] = language.wrong_password
                
            else:
                request.user.set_password(newpassword)
                request.user.save()
                response['success'] = 'true'
                response['error_message'] = ''
                
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')
    
    else:
        raise Http404

@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/seiscreen/login/')
    
