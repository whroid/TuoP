from django.db import models
from sso.models import User
# Create your models here.

class Topic(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=200)
	create_time = models.DateField('create_time')

	def __unicode__(self):
		return self.title

class Vote(models.Model):
	topic = models.ForeignKey(Topic)
	user = models.ForeignKey(User)

