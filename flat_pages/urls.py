from django.conf.urls.defaults import *

urlpatterns = patterns('flat_pages.views',
        url(r'^(?P<slug>[\w|-]+)/$', 
            'detail', 
            {'template_name': 'flat_pages/detail.html'},
            name='flat_pages_detail'),
)
