# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	print '***INDEX***' * 200
	return render(request, 'login/index.html')

def login(request):
	print 'login'*250

def register(request):
	print 'register'* 250

def home(request):
	print 'home'*250