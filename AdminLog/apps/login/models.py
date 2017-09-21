# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
import re

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def RegisterUser(self, postData):
		status = {'valid':True, 'errors':[], 'user':None}
		if not postData['name']:
			status['valid'] = False
			status['errors'].append('Enter a real name')
		if not postData['username'] or len(postData['username'])<3:
			status['valid'] = False
			status['errors'].append('Pick a better username')
		if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"):
			status['valid'] = False
			status['errors'].append('That email is shit')
		if not postData['password'] or len(postData['password'])< 8:
			status['valid'] = False
			status['errors'].append('Password is too WEAK')
		if postData['confirmPassword'] != postData['confirmPassword']:
			status['valid'] = False
			status['errors'].append('Passwords do not match')
		if status['valid'] is False:
			return status

		user = User.objects.filter(username=postData['username'])

		if user:
			status['valid']=False
			status['errors'].append('Failed to Register new user')

		if status['valid']:
			try:
				hashpass = (bcyrpt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
				user = User.objects.create(name=postData['name'], username=postData['username'], email=postData['email'], password=hashpass)
				user.save()
				status['user'] = user

			except IntegrityError as e:
				status['valid'] = False
				if 'UNIQUE constraint' in e.message:
					status['errors'].append('User already exists')
				else:
					status['errors'].append(e.message)

		return status

	def LoginUser(self, postData):
		status = {'valid': True, 'errors':[], 'user':None}



class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()