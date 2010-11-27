from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse


from problems.models import Problem
from problems.forms import QuestionForm

def index(request, template_name=None):
    """Display a list of problems.
    """
    problems = Problem.objects.all()
    return render_to_response(template_name, {'problems': problems})

def detail(request, pk, template_name=None):
    """Display the problem and handle the user's answer.
    """
    problem = get_object_or_404(Problem, pk=pk).cast()
    if request.method == 'POST':
        form = problem.get_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('problems_right', args=[pk]))
    else:
        form = problem.get_form()

    return render_to_response(template_name,
                              {'problem': problem,
                               'form': form},
                              context_instance=RequestContext(request))

def right_answer(request, pk, template_name=None):
    """A view which tells the user they are right.
    """
    problem = get_object_or_404(Problem, pk=pk).cast()
    return render_to_response(template_name, {'problem': problem})
