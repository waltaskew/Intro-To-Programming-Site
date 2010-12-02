from django.db import models
from problems.forms import QuestionForm
from utils.models import InheritanceCastModel

class Problem(InheritanceCastModel):
    """Base class for problems and solutions.
    """
    title = models.CharField(max_length=255)
    number = models.DecimalField(max_digits=4, decimal_places=3)
    difficulty = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    errata = models.FileField(upload_to='program_descriptions',
            null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('number', 'title')
    
    def __unicode__(self):
        """String representation of the instance.
        """
        return '%s - %s' % (self.number, self.title)

class Question(Problem):
    """A simple question and answer pair.
    """
    answer = models.CharField(max_length=255)

    def get_form(self, *args, **kwargs):
        """Return a form to answer the question.
        """
        form = QuestionForm(*args, **kwargs)
        form.problem = self
        return form

class Program(Problem):
    """A problem which requires the user to upload a program 
    they have written.
    """
    tester = models.FileField(upload_to='program_testers', 
            null=True, blank=True)
