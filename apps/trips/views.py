from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Trip
from ..login.models import User
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
	logged_in = request.session['logged_in']
	context = {
		"user" : User.objects.get(id=request.session['logged_in']),
		"trips" : Trip.objects.all(),
	}
	return render(request, 'trips/index.html', context)

# def createUser(request):
# 	userdata = request.POST
# 	results = User.userManager.validate(userdata)
# 	user = User.objects.get(id=results[2])

# 	if results[0] == True:
# 		return redirect(reverse('travel_index', kwargs={'id':request.session['logged_in']}))
# 	else: 
# 		return redirect(reverse('login_index'))

# def login(request):
# 	logindata = request.POST
# 	results = User.userManager.login(logindata)
# 	if results[0] == True:
# 		if 'logged_in' not in request.session:
# 			request.session['logged_in'] = User.objects.filter(username__exact=logindata['username']).id
# 			return redirect(reverse('travel_index', kwargs={'id':request.session['logged_in']}))
# 	else:
# 		return redirect (reverse('login_index'))

def addTrip(request):
	logged_in = request.session['logged_in']
	context = {
		"user" : User.objects.get(id=request.session['logged_in'])
	}
	print context['user']
	return render(request, 'trips/addTrip.html', context)

def createTrip(request):
	logged_in = request.session['logged_in']
	tripdata = request.POST
	ownerdata = {
		"user_id" : User.objects.get(id=request.session['logged_in'])
	}


	results = Trip.tripManager.createTrip(tripdata, ownerdata, request)

	if results[0] == True:
		return redirect(reverse('travel_index'))
	else: 
		return redirect(reverse('travel_addTrip'))
	# return render(request, 'trips/addTrip.html')
	


def showTrip(request, id):
	context = {
		"trips": Trip.objects.get(id=id),
		"users": User.objects.all()
	}
	return render(request, 'trips/showTrip.html', context)

def joinTrip(request, id):
	user = User.objects.get(id=request.session['logged_in'])
	trip = Trip.objects.get(id=id)
	trip.travelers = user
	trip.save()
	return render(request, 'trips/showTrip.html')

def logout(request):
	request.session.clear()
	return redirect (reverse('login_index'))




# def logout(request):
# 	request.session.clear()
# 	return redirect (reverse('login_index'))