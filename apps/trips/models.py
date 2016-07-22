from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from ..login.models import User

from datetime import datetime

class TripManager(models.Manager):
	def createTrip(self, tripdata, ownerdata, request):
		errors = False

		if len(tripdata['destination']) < 1:
			messages.warning(request, "City cannot be blank.")
			errors = True

		if len(tripdata['description']) < 1:
			messages.warning(request, "Description cannot be blank.")
			errors = True

		if len(tripdata['start_date']) < 1:
			messages.warning(request, "Description cannot be blank.")
			errors = True
		elif datetime.today().date() > datetime.strptime(tripdata['start_date'], '%Y-%m-%d').date():
			messages.warning(request, "Start date cannot be in the past.")
			errors = True

		if len(tripdata['end_date']) < 1:
			messages.warning(request, "Description cannot be blank.")
			errors = True
		elif tripdata['end_date'] < tripdata['start_date']:
			messages.warning(request, "End date cannot be before start date.")
			errors = True

		if errors:
			return (False, messages)
		else:
			trip = self.create(start_date=tripdata['start_date'], end_date=tripdata['end_date'], description=tripdata['description'],owner=ownerdata['user_id'],destination=tripdata['destination'])
			
			return(True, tripdata, trip.id)

	def joinTrip(self, trip, user, request):
		trip = Trip.objects.get(id=trip)
		trip.traveler = user
		trip.save()
		return trip

class Trip(models.Model):
	description = models.CharField(max_length=255)
	start_date = models.DateField()
	end_date = models.DateField()
	traveler = models.ManyToManyField(User, related_name='travelers', blank=True)
	owner = models.ForeignKey(User, related_name='trip_owner')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	tripManager = TripManager()
	objects = models.Manager()
	destination = models.CharField(max_length=255)




# Create your models here.
