# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
	return render(request, 'Log_Reg/index.html')
	print "**INDEX**" * 1000

def register(request):
	status = User.objects.registerUser(request.POST)
	if not status['valid']:
		for error in status['error']:
			messages.error(request, error)
			return redirect('/')
	request.session['id'] = status['user'].id
	return redirect('welcome')

	print "**REGISTER**" * 250

def login(request):
	status = User.objects.loginUser(request.POST)
	if status['valid'] is False:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	else:
		user = User.objects.get(id=status['user'])
		request.session['id'] = user.id
	return redirect('welcome')
	print "**LOGIN**" * 250

def welcome(request):
	return render(request, 'Log_Reg/welcome.html')
