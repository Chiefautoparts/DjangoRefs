# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
import re

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	


class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()