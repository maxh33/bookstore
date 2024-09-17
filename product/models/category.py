from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title