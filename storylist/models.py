from django.db import models

class Story(models.Model):
    headline = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    source = models.CharField(max_length=50)
    added = models.DateTimeField()

    def __unicode__(self):
    	return u'%s: %s' % (self.source, self.headline)