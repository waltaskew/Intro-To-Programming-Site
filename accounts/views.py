from accounts.forms import RegistrationForm
from accounts.models import UserProfile

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def register(request, template_name=None):
    """Handle user registration.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.create(user=user)
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('problems_index'))
    else:
        form = RegistrationForm()
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=RequestContext(request))
