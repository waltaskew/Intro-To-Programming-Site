from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from problems.models import Problem


# Create a Dispatcher; this handles the calls and translates info to function maps.
dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None) # Python 2.5

 
@csrf_exempt
def rpc_handler(request):
    """Send xml rpc requests to the dispatcher.
    """
    if request.POST:
        response = HttpResponse(mimetype="application/xml")
        response.write(dispatcher._marshaled_dispatch(request.raw_post_data))
    else:
        response = HttpResponse()
    response['Content-length'] = str(len(response.content))
    return response


def login(username, password):
    """If a valid username and passowrd are provided, then
    return the user id for the logged in user ans a token
    to be used for future xml rpc transactions.
    """
    user = authenticate(username=username, password=password)
    if user is None:
        return 0, 0
    else:
        return user.id, user.get_profile().secret_key

def add_answer(secret_key, user_id, problem_id):
    """Record a correct answer for the problem with id problem_id
    on behalf of username.
    """
    user = User.objects.get(pk=user_id)
    profile = user.get_profile()
    if profile.secret_key == secret_key:
        problem = Problem.objects.get(pk=problem_id)
        user.get_profile().add_answer(problem)
        return True
    else:
        raise TypeError("Incorrect secret key %s given" % secret_key)

dispatcher.register_function(login, 'login')
dispatcher.register_function(add_answer, 'add_answer')
