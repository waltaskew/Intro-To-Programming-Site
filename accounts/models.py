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

    def add_answer(self, problem, program=None):
        """Add an answer to a problem for the user.
        """
        answer, created = Answer.objects.get_or_create(answered_by=self.user,
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
        return Problem.objects.all().filter(answer__answered_by=self.user)

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
    answered_by = models.ForeignKey(User)
    program = models.FileField(upload_to=get_path, null=True, blank=True)






