from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Persona(models.Model):
    """A person in a dream, real and anonymized information"""
    common_name = models.TextField(
            help_text="Short name the persona commonly goes by (e.g. first name, or nickname)")
    full_name = models.TextField(help_text="Full name of this persona")
    anon_always = models.BooleanField(default=False,
            help_text="This name is always anonymized whether the post is anonymouse or not")
    bio = models.TextField(help_text="Brief description of this person")
    gender = models.CharField(max_length=1, blank=True)
    gender_priv = models.IntegerField(default=0)
    birthdate = models.DateField(blank=True)
    birthdate_priv = models.IntegerField(default=0)
    country = models.TextField(max_length=250)
    city = models.TextField(max_length=250)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(User)

class Profile(models.Model):
    master_persona = models.ForeignKey(Persona, blank=True)
    default_privacy = models.IntegerField(default=0)



class Dream(models.Model):
    title = models.TextField()
    body = models.TextField()
    comment = models.TextField()
    dream_date = models.DateTimeField(blank=True)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)
    status = models.IntegerField(default=False)
    dreamer = models.ForeignKey(Persona)
    vividness = models.IntegerField(blank=True,
            help_text = 'how clear is your rememberance of the dream')
    negative_positive = models.IntegerField(blank=True,
            help_text = '1 = negative (nightmare), 5 = neutral, 9 = positive (joyful)')

class DreamRating(models.Model):
    dream = models.ForeignKey(Dream)
    rating = models.IntegerField()
    created = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User)

class TagType(models.Model):
    """Type of tag: mood, dream type, user (used for classifying tags)"""
    name = models.TextField()


class Tag(models.Model):
    name = models.TextField()
    type = models.ForeignKey(TagType)
    date = models.DateTimeField()
    origin = models.ForeignKey(User, blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, related_name="tags")
    dream = models.ManyToManyField(Dream, through="DreamTag")


class DreamTag(models.Model):
    dream = models.ForeignKey(Dream)
    tag = models.ForeignKey(Tag)
    tagged = models.DateTimeField(default=now)






