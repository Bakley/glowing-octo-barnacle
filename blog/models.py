from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# First, define the Manager subclass.
class PublishedManager(models.Manager):
    """
    because get_queryset() returns a QuerySet object, you can use filter(), exclude() and all the other QuerySet 
    methods on it.
    """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Then hook it into the model explicitly.
class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')
    object = models.Manager()  # the default manager
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_details',
                       args=[
                           self.publish.year,
                           self.publish.strftime('%m'),
                           # using the strftime() function to build the URL using month and day with leading zeros
                           self.publish.strftime('%d'),
                           self.slug,
                       ])
