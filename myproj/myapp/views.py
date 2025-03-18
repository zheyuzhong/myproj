from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse
def sayhello(request):
	return HttpResponse("Hello 劉老師!")
def hello2(request, username):
	return HttpResponse("Hello 2 " + username)
def hello3(request, username):
	now=datetime.now()
	return render(request, "hello3.html",locals())
def hello4(request, username):
	now=datetime.now()
	return render(request, "hello4.html",locals())