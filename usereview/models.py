"""
This module contains model definition for Movies
"""
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

class Movies(models.Model):
    """
    Movie table information
    """
    movie_name = models.TextField(default="")

class Usereview(models.Model):
    """
    Usereview table information
    """
    name = models.TextField(default="")
    rating = JSONField(default=[])
    comments = JSONField(default=[])
