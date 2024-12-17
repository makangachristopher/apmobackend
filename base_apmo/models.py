from django.db import models
from django.contrib.auth.models import User
from social_links_field.models import SocialLinksField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Sermon(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    preacher = models.ForeignKey(
        'Preacher', on_delete=models.CASCADE, related_name="sermons", verbose_name=_("Preacher")
    )
    duration = models.DurationField(verbose_name=_("Duration"))  # Store duration in HH:MM:SS format
    date_published = models.DateField(verbose_name=_("Date Published"))
    audio_file = models.FileField(upload_to='audio/sermons/', verbose_name=_("Audio File"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"))
    topic = models.CharField(max_length=255, verbose_name=_("Topic"))
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name="sermons", verbose_name=_("Category")
    )
    playlists = models.ManyToManyField(
        'Playlist', related_name="sermons", blank=True, verbose_name=_("Playlists")
    )
    tags = models.CharField(max_length=255, blank=True, verbose_name=_("Tags"))  # Comma-separated tags
    language = models.CharField(max_length=50, verbose_name=_("Language"))
    play_count = models.PositiveIntegerField(default=0, verbose_name=_("Play Count"))
    likes_count = models.PositiveIntegerField(default=0, verbose_name=_("Likes Count"))
    bg_picture = models.ImageField(upload_to='images/sermons/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.preacher.name}"


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Preacher(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='images/preachers/', null=True, blank=True)
    social_links = SocialLinksField(null=True, blank=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    # sermons = models.ManyToManyField(Sermon, related_name='playlists', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
