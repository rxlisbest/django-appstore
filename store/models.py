from django.db import models

class appClass(models.Model):
	c_title = models.CharField(max_length=50)
	c_path = models.CharField(max_length=20)
	c_sort = models.IntegerField(default=0)
	def __unicode__(self):
		return self.c_title
	
class apps(models.Model):
	c = models.ForeignKey(appClass)
	a_title = models.CharField(max_length=100)
	a_url = models.CharField(max_length=255)
	a_sort = models.IntegerField(default=0)