import os.path

from django.contrib.auth.models import User
from django.db import models

from problems.models import Problem

def get_path(instance, filename):
    """Return a path for the user to upload files to.
    """
    username = instance.answered_by.user.username
    return os.path.join('programs', username, filename)

class UserProfile(models.Model):
    """User profile for the user accounts.
    """
    user = models.OneToOneField(User)
    total_answered = models.IntegerField()

    def __unicode__(self):
        """String representation of the instance.
        """
        return 'User Profile for %s' % self.user

    def add_answer(self, problem, program=None):
        """Add an answer to a problem for the user.
        """
        answer, created = Answer.objects.get_or_create(answered_by=self,
                                                       problem=problem)
        if created:
            self.total_answered += 1
            self.save()
        if program is not None:
            answer.program = program
        return answer.save()

    def get_answered_problems(self):
        """Return the problems that the user has answered.
        """
        return Problem.objects.all().filter(answer__answered_by=self)

    def is_answered(self, problem):
        """Return a boolean idicating whether a given problem
        has been solved by the user.
        """
        return bool(Answer.objects.all().filter(answered_by=self,
                                                problem=problem))

    def save(self, *args, **kwargs):
        """Initialiaze the created count."""
        if not self.id:
            self.total_answered = 0
        return super(UserProfile, self).save(*args, **kwargs)

class Answer(models.Model):
    """An answer to a question.
    """
    created = models.DateField(auto_now=True, auto_now_add=True)
    problem = models.ForeignKey(Problem)
    answered_by = models.ForeignKey(UserProfile)
    program = models.FileField(upload_to=get_path, null=True, blank=True)

    def __unicode__(self):
        """String representation of the instance.
        """
        return '%s answered by %s' % (self.problem, self.answered_by.user)