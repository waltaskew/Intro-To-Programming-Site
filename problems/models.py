from django.db import models
from problems.forms import QuestionForm


class ProblemManager(models.Manager):
    """Custom maanager for the Problem mode.
    """
    def actives(self):
        """Return all active problems.
        """
        return self.all().filter(active=True)


class Problem(models.Model):
    """Model for problems given to students.
    """
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    number = models.DecimalField(max_digits=3, decimal_places=2)
    difficulty = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    answer = models.CharField(max_length=255, blank=True)
    created = models.DateField(auto_now_add=True)

    objects = ProblemManager()
    
    class Meta:
        ordering = ('-number', 'title')
    
    def __unicode__(self):
        """Returns a string representation of the instance.
        """
        return '%s - %s' % (self.number, self.title)

    def get_form(self, *args, **kwargs):
        """Return a form to answer the question.
        """
        answer = self.answer
        if answer:
            form = QuestionForm(*args, **kwargs)
            form.answer = answer
            return form
        else:
            return None

    def get_files(self):
        """Returns the files associated with this problem.
        """
        return ProblemFile.objects.all().filter(problem=self)
    
class ProblemFile(models.Model):
    """Represents a file that is attached to a problem.
    """
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='problems_documents')
    problem = models.ForeignKey(Problem)
    created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        """Returns a string representation of the instance.
        """
        return '%s for %s' % (self.title, self.problem)

    def get_link(self):
        """Returns a link to the file.
        """
        return self.document.url
