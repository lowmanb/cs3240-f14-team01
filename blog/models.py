from django.db import models
from django.core.urlresolvers import reverse

class UploadFile(models.Model):
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.slug
#simple tag
class Tag(models.Model):

    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


#this is needed for home page
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


# "bulletin" class
class Entry(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    file = models.ForeignKey(UploadFile)

    objects = EntryQuerySet.as_manager()

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
    
    
    def __str__(self):
        return self.title
