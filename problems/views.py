from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from problems.models import Problem

@login_required
def index(request, template_name=None):
    """Display a list of problems.
    """
    problems = Problem.objects.actives()
    answered_problems = request.user.get_profile().get_answered_problems()
    answered_problems = dict([(problem, None) for problem in answered_problems])
    return render_to_response(template_name, {'problems': problems,
                                              'answered_problems': answered_problems})

@login_required
def detail(request, pk, template_name=None):
    """Display the problem and handle the user's answer.
    """
    problem = get_object_or_404(Problem, pk=pk)
    is_answered = request.user.get_profile().is_answered(problem)
    files = problem.get_files()
    if request.method == 'POST':
        form = problem.get_form(request.POST)
        # The form could be None if the user is doing a post
        # on the detail page of a problem without an answer form.
        if form is None:
            return HttpResponseRedirect(reverse('problems_detail', args=[pk]))
        elif form.is_valid():
            request.user.get_profile().add_answer(problem)
            return HttpResponseRedirect(reverse('problems_right', args=[pk]))
    else:
        form = problem.get_form()

    return render_to_response(template_name,
                              {'problem': problem,
                               'is_answered': is_answered,
                               'files': files,
                               'form': form},
                              context_instance=RequestContext(request))

@login_required
def right_answer(request, pk, template_name=None):
    """A view which tells the user they are right.
    """
    problem = get_object_or_404(Problem, pk=pk)
    return render_to_response(template_name, {'problem': problem})
