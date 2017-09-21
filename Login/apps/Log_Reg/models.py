# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def registerUser(self, postData):
		status = {'valid': True, 'errors': [], 'user': None}
		if not postData['firstName'] or len(postData['firstName']) < 3:
			status['errors'].append("First Namemust be at least 3 characters long you DUMBASS!!!!!!")
			status['valid'] = False
		if not postData['lastName'] or len(postData['lastName']) < 3:
			status['error'].append("That last name is stupid pick another one")
			status['valid'] = False
		if not postData['username'] or len(postData['username']) < 3:
			status['errors'].append("You must be a special kind of stupid")
			status['valid'] = False
		if not postData['email'] or not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email):
			status['errors'].append("Email is about as fake as CNN's news")
			status['valid'] = False
		if not postData['password'] or len(postData['password']) < 8:
			status['errors'].append('That password is so easy Russia Did not need to hack your account the doors wide open')
			status['valid'] = False
		if postData['confPassword'] != postData['password']:
			status['errors'].append('really??? you can\'t even spell a word the sane  twice.... this is why the world laughs at us')
			status['valid'] =False
			
		if status['valid'] is False:
			return status
		user = User.objects.filter(username=postData['username'])
		if user:
			status['valid'] = False
			status['errors'].append("Congrats you now have the smae intellegence to run North Korea, but not enough to register for this site")
		if status['valid']:
			password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user =User.objects.create(
				firstName = postData['firstName'],
				lastName = postData['lastName'],
				email=postData['email'],
				username=postData['username'],
				password = password)
			status['user'] = user
		return status

	def loginUser(self, postData):
		status = {'valid': True, 'errors': [], 'user': None}
		user = User.objects.filter(username=postaData['username'])
		try:
			user[0]
		except IndexError:
			results['status'] = False
			results['errors'].append("Failure at Life and to login in.")
			return status
		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(),
												user[0].password.encode()):
				status['valid'] = False
				status['errors'].append('Fucked up logging in again')
			else:
				status['user'] = user[0].id
		else:
			status['valid'] = False
		return status
		

class User(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	username =models.CharField(max_length=255)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length= 100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id) + ", " + self.username
	objects = UserManager()