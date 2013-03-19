from django.conf.urls import *

urlpatterns = patterns('problems.views',
        url(r'^$', 
            'index', 
            {'template_name': 'problems/index.html'},
            name='problems_index'),
        url(r'^(?P<pk>\d+)/$', 
            'detail', 
            {'template_name': 'problems/detail.html'},
            name='problems_detail'),
        url(r'^(?P<pk>\d+)/right$', 
            'right_answer', 
            {'template_name': 'problems/right.html'},
            name='problems_right'),
)
