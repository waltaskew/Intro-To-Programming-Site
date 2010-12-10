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

def add_answer(username, password, problem_id):
    """Record a correct answer for the problem with id problem_id
    on behalf of the user user with the given credentials.
    """
    user = authenticate(username=username, password=password)
    if user is None:
        raise TypeError("Incorrect username and passowrd given")
    else:
        problem = Problem.objects.get(pk=problem_id)
        user.get_profile().add_answer(problem)
        return True

dispatcher.register_function(add_answer, 'add_answer')
