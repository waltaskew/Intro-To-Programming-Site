from django.conf.urls import *

urlpatterns = patterns('',
        url(r'^login/$', 
            'django.contrib.auth.views.login', 
            {'template_name': 'accounts/login.html'},
            name='accounts_login'),
        url(r'^logout/$', 
            'django.contrib.auth.views.logout',
            {'next_page': '/accounts/login/'},
            name='accounts_logout'),
        url(r'^register/$', 
            'accounts.views.register',
            {'template_name': 'accounts/register.html'},
            name='accounts_register'),
)
