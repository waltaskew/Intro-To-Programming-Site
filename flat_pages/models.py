from django.db import models
from django.template.defaultfilters import slugify

class FlatPage(models.Model):
    """Model for problems given to students.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    text = models.TextField()
    modified = models.DateField(auto_now=True)

    def save(self):
        """Create a slug if one has not been provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super(FlatPage, self).save()

    def __unicode__(self):
        """Returns the page's title.
        """
        return self.title
