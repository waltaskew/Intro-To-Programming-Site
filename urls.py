from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'problems.views.index', {'template_name': 'problems/index.html'}),
    (r'^problems/', include('problems.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/var/django/homework/static'}),
    (r'^admin/', include(admin.site.urls)),
)