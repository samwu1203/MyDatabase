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
from PIL import Image, ExifTags
from django.dispatch import receiver
from django.db.models.signals import post_save
import os

def rotate_image(filepath):
	try:
		image = Image.open(filepath)
		for orientation in ExifTags.TAGS.keys():
			if ExifTags.TAGS[orientation] == 'Orientation':
				break
		exif = dict(image._getexif().items())

		if exif[orientation] == 3:
			image = image.rotate(180, expand=True)
		elif exif[orientation] == 6:
			image = image.rotate(270, expand=True)
		elif exif[orientation] == 8:
			image = image.rotate(90, expand=True)
		image.save(filepath)
		image.close()
	except (AttributeError, KeyError, IndexError):
	# cases: image don't have getexif
		pass


class mysearch(models.Model):
	timezone.localtime(timezone.now())
	Class = models.CharField(blank=True, null=True, max_length=200)
	title = models.CharField(blank=True, null=True, max_length=200)
	content = models.TextField(blank=True, null=True, max_length=2000)
	created_data = models.DateTimeField(blank=True,null=True)
	publish_data = models.DateTimeField(default=timezone.now)
	file = models.FileField(blank=True,upload_to = './file/')
	img = models.ImageField(blank=True,upload_to='./img')
	
@receiver(post_save, sender=mysearch, dispatch_uid="update_image_profile")
def update_image_profile(sender, instance, **kwargs):
  if instance.img:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.img.url
    rotate_image(fullpath)

#	def __unicode__(self):
#		return self.title