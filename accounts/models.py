from django.contrib.auth.models import User
from django.db import models

from problems.models import Problem


class UserProfile(models.Model):
    """User profile for the user accounts.
    """
    user = models.OneToOneField(User)
    total_answered = models.IntegerField()

    def __unicode__(self):
        """String representation of the instance.
        """
        return 'User Profile for %s' % self.user

    def add_answer(self, problem):
        """Add an answer to a problem for the user.
        """
        answer, created = Answer.objects.get_or_create(answered_by=self,
                                                       problem=problem)
        if created:
            self.total_answered += 1
            self.save()

    def get_answered_problems(self):
        """Return the problems that the user has answered.
        """
        answers = Answer.objects.all().filter(answered_by=self)
        problem_ids = answers.values_list('problem', flat=True)
        return Problem.objects.all().filter(pk__in=list(problem_ids))

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
    problem = models.ForeignKey(Problem, related_name='given_answer')
    answered_by = models.ForeignKey(UserProfile)

    def __unicode__(self):
        """String representation of the instance.
        """
        return '%s answered by %s' % (self.problem, self.answered_by.user)
