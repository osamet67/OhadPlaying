from django.db import models
from django import forms

# Create your models here.
class LogLine (models.Model):
	logtext = models.CharField(max_length=255)
	place = models.IntegerField()

class Log (models.Model):
	log_dt = models.DateTimeField()
	account = models.CharField(max_length=255)
	agent = models.CharField(max_length=255)
	text = models.CharField(max_length=255)

class LogForm (forms.Form):
	logline = forms.CharField(max_length=255)	
