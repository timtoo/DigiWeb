from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    gender = models.CharField(max_length=1, default='U')


class Location(models.Model):
    """A location in the dream"""
    name = models.TextField()
    city = models.TextField(blank=True)
    address = models.TextField(blank=True)
    anon_always = models.BooleanField(default=False,
            help_text="Always use anonymous name for this location")
    anon_name = models.TextField(blank=True)
    anon_city = models.TextField(blank=True)
    anon_address = models.TextField(blank=True)


class Persona(models.Model):
    """A person in a dream, real and anonymized information"""
    common_name = models.TextField(
            help_text="The name this person is referred to as in dreams (should be unique for anonamizing purposes)")
    full_name = models.TextField(help_text="Full name of this persona")
    anon_always = models.BooleanField(default=False,
            help_text="This name is always anonymized whether the post is anonymouse or not")
    gender = models.CharField(max_length=1, blank=True)
    birthday = models.DateField(blank=True)
    bio = models.TextField(help_text="Brief description of this person")
    relationship = models.IntegerField(help_text="Relationship to the dreamer in real life")
    anon_alias = models.TextField(blank=True,
            help_text="Name to use instead of the 'common' or 'full' name when anonymizing")
    anon_birthday = models.DateField(blank=True)
    anon_bio = models.TextField(help_text="Anonymized brief description of this person")
    owner = models.ForeignKey(User)


class Dream(models.Model):
    title = models.TextField()
    body = models.TextField()
    dream_date = models.DateTimeField(blank=True)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    status = models.IntegerField(default=False)
    dreamer = models.ForeignKey(User, related_name="dreams")
    vividness = models.IntegerField(blank=True,
            help_text = 'how clear is your rememberance of the dream')
    negative_positive = models.IntegerField(blank=True,
            help_text = '1 = negative (nightmare), 5 = neutral, 9 = positive (joyful)')


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
    tagged = models.DateTimeField(default=datetime.now())






