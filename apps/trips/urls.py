from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^trips$', views.index, name="travel_index"),
    url(r'^logout$', views.logout, name="logOut"),
    url(r'^trips/add$', views.addTrip, name="travel_addTrip"),
    url(r'^trips/add/submit$', views.createTrip, name="travel_createTrip"),
    url(r'^trips/(?P<id>\d+)$', views.showTrip, name="travel_showTrip"),
    url(r'^trips/(?P<id>\d+)/join$', views.joinTrip, name="travel_joinTrip"),
]