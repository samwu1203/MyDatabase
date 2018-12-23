# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class mysearch(models.Model):
	timezone.localtime(timezone.now())
	Class = models.CharField(blank=True, null=True, max_length=200)
	title = models.CharField(blank=True, null=True, max_length=200)
	content = models.TextField(blank=True, null=True, max_length=2000)
	created_data = models.DateTimeField(blank=True,null=True)
	publish_data = models.DateTimeField(default=timezone.now)
	file = models.FileField(blank=True,upload_to = './file/')
	img = models.ImageField(blank=True,upload_to='./img')

	def __unicode__(self):
		return self.title