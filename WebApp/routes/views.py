from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import simplejson

from routes.models import Route
from routes.models import Point
from mobileUsers.models import MobileUser
# Create your views here.

def routes(request):
	_id = request.POST.get("remove", "")
	if _id:
		Route.objects.filter(id=int(_id.split('#')[1])).delete()

	routes = Route.objects.all()
	return render_to_response("routes.html",
								locals(),
								context_instance=RequestContext(request))

def routeDetails(request, num):
	routeId= num
	points = Point.objects.filter(Route_id=num)
	return render_to_response("routeDetails.html",
								locals(),
								context_instance=RequestContext(request))

def routeOnMap(request, num):
	routeId= num
	lats = Point.objects.filter(Route_id=num).values('Latitude')
	lons = Point.objects.filter(Route_id=num).values('Longitude')
	adds = Point.objects.filter(Route_id=num).values('Address')

	latsList = []
	lonsList = []
	addsList = []
	for lat in lats:
		latsList.extend(lat.values())

	for lon in lons:
		lonsList.extend(lon.values())

	for add in adds:
		addsList.append(str(add.values()[0]))

	json_list = simplejson.dumps(latsList)
	json_list = simplejson.dumps(lonsList)
	json_list = simplejson.dumps(addsList)

	return render_to_response("routeOnMap.html",
								locals(),
								context_instance=RequestContext(request))

def setRoute(request, num):
	mobileUser = MobileUser.objects.get(pk=num)
	routes = Route.objects.all()
	_id = request.POST.get("set", "")
	if _id:
		route = Route.objects.get(pk=int(_id.split('#')[1]))
		route.mobileUser = mobileUser
		route.save()
		return HttpResponseRedirect('mobileUsers')

	return render_to_response("setRoute.html",
								locals(),
								context_instance=RequestContext(request))
