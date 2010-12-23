from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404

from flat_pages.models import FlatPage

@login_required
def detail(request, slug, template_name=None):
    """Display the requested flat page.
    """
    page = get_object_or_404(FlatPage, slug=slug)
    return render_to_response(template_name, {'page': page})
