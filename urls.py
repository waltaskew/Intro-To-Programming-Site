from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'problems.views.index', {'template_name': 'problems/index.html'}),
    (r'^problems/', include('problems.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^pages/', include('flat_pages.urls')),
    (r'^xml_rpc_srv/', 'xmlrpc.handler.rpc_handler'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
    (r'^admin/', include(admin.site.urls)),
)
