from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from routes.api import RouteResource
from points.api import PointResource
from trackingPoints.api import TrackingPointResource
from trackingRoutes.api import TrackingRouteResource
from address.api import AddressResource
from mobileUsersRoutes.api import MobileUsersRouteResource
from mobileUsers.api import MobileUserResource

admin.autodiscover()

#resources (tastypie)
route_resource = RouteResource()
point_resource = PointResource()
trackingPoint_resource = TrackingPointResource()
trackingRoute_resource = TrackingRouteResource()
mobileUsersRoutes_resource = MobileUsersRouteResource()
address_resource = AddressResource()
mobileUser_resource = MobileUserResource()


urlpatterns = patterns('',

	#home
        url(r'^$', 'home.views.home', name='home'),
        url(r'^home.html$', 'home.views.home', name='home'),

        #mobileUsers
	url(r'^mobileUsers$', 'mobileUsers.views.mobileUsers', name='mobileUsers'),
	url(r'^addMobileUser$', 'mobileUsers.views.addMobileUser', name='addMobileUser'),
	url(r'^mobileUsersRoutes(?P<num>\d+)$','mobileUsersRoutes.views.mobileUsersRoutes'),
	url(r'^trackMobileUser(?P<num>\d+)$', 'mobileUsersRoutes.views.trackMobileUser', name='trackMobileUser'),
	url(r'^mobileUserHistory(?P<num>\d+)$', 'mobileUsersRoutes.views.mobileUserHistory', name='mobileUserHistory'),

	#routes
	url(r'^routes$', 'routes.views.routes', name='routes'),
	url(r'^newRoute$', 'map.views.newRoute', name='newRoute'),
	url(r'^routes$', 'routes.views.routes', name='routes'),
	url(r'^routeDetails(?P<num>\d+)$', 'routes.views.routeDetails', name='routeDetails'),
	url(r'^routeOnMap(?P<num>\d+)$', 'routes.views.routeOnMap', name='routeOnMap'),
	url(r'^saveRoute/$','map.views.saveRoute'),
	url(r'^setRoute(?P<num>\d+)$','mobileUsersRoutes.views.setRoute'),
        url(r'^setUserToRoute(?P<num>\d+)$','mobileUsersRoutes.views.setUserToRoute'),
        url(r'^trackAll$','trackingRoutes.views.trackAll'),

	#webAppUsers
	url(r'^webAppUsers$', 'webAppUser.views.webAppUsers', name='webAppUsers'),
	url(r'^addWebUser$', 'webAppUser.views.addWebUser', name='addWebUser'),

	#tastyPie
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/', include(route_resource.urls)),
        url(r'^api/', include(point_resource.urls)),
        url(r'^api/', include(address_resource.urls)),
        url(r'^api/', include(mobileUser_resource.urls)),
        url(r'^api/', include(mobileUsersRoutes_resource.urls)),
        url(r'^api/', include(trackingPoint_resource.urls)),
        url(r'^api/', include(trackingRoute_resource.urls)),
        url(r'^loginPage','Login.views.loginWebAppUser'),
	url(r'^invalidLogin','Login.views.invalidLogin'),
	url(r'^logoutPage', 'Login.views.user_logout', name='logout'),

        #authentication
        url(r'^loginPage$','Login.views.loginWebAppUser'),
	url(r'^invalidLogin$','Login.views.invalidLogin'),
	url(r'^logoutPage$', 'Login.views.user_logout', name='logout'),
	
)
