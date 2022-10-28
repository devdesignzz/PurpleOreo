from django.db import models
from django.contrib.auth.models import User
from .helpers import *
from django.urls import reverse
import datetime


# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    confess = models.CharField(max_length=200, null=True, blank=True)
    short_story = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.date.today())
    stay_hidden = models.BooleanField(default=False, help_text='Stay Anonymous')
    slug = models.SlugField(max_length=1001)

    def __str__(self):
        return self.confess + ' | ' + str(self.author.first_name)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.confess)
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('index')