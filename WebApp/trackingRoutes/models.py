from django.db import models
from django.utils.encoding import smart_unicode

class TrackingRoute(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)

def __unicode__(self):
	return smart_unicode(self.id)
