#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import mysearch
from .forms import PostForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
import os, sys
#from PIL import Image, ExifTags

#def rotate_image(filepath):
#	try:
#		image = Image.open(filepath)
#		for orientation in ExifTags.TAGS.keys():
#			if ExifTags.TAGS[orientation] == 'Orientation':
#				break
#		exif = dict(image._getexif().items())

#		if exif[orientation] == 3:
#			image = image.rotate(180, expand=True)
#		elif exif[orientation] == 6:
#			image = image.rotate(270, expand=True)
#		elif exif[orientation] == 8:
#			image = image.rotate(90, expand=True)
#		image.save(filepath)
#		image.close()
#	except (AttributeError, KeyError, IndexError):
	# cases: image don't have getexif
#		pass

@csrf_exempt
def post_list(request):
	form=PostForm()
	return render(request,'blog/post_list.html',{'form':form})

@csrf_exempt
def post_list1(request):
	if request.method=="POST":
#		img=request.FILES['img']
#		img.save('myphoto.jpg', content, save=True)
#		file=request.FILES['file']
#		file.save('file', content, save=True)
#		data=request.POST
#		print (data)
#		data=data.split('\r\n')
#		Class=str(data[1]).split('=')[1]
#		title=str(data[2]).split('=')[1]
#		content=str(data[3]).split('=')[1]
#		created_data=str(data[4]).split('=')[1]
#		publish_data=str(data[5]).split('=')[1]
#		POST = {'Class': Class,
#				'title': title,
#				'content': content,
#				'created_data': created_data,
#				'publish_data': publish_data,}
		form = PostForm(request.POST, request.FILES)
#		print (request.FILES['img'])
#		img=request.FILES['img']
		if form.is_valid():
			form.save()
			form = PostForm()
#			post=mysearch.objects.order_by('id').last()
#			print (str(post.img))
#			rotate_image('./media/'+str(post.img))
			posts = mysearch.objects.all()
			return render(request, 'blog/post_list.html',{'form':form, 'posts':posts})
		print ('error')
		return render(request, 'blog/post_list.html',{'form':form})
#			title = form['title']
#			content = form['content']
#			model_name = form['model_name']
#			created_data = form['created_data']
#			mysearch.objects.create(title = 'title', content = 'content', model_name = 'model_name', created_data = 'created_data')
#			form = Comment (title=title,content=content,model_name=model_name,created_data=created_data)
#			form.save()
#			print('error')
#			POST = {'title': 'NG',
#					'content': 'NG',
#					'model_name': 'NG',}
#			form = PostForm(POST)
#			form.save()
#			return render(request, 'blog/post_list1.html',{'form': form},{'posts':posts},context_instance=RequestContext(request))
	else:
		form = PostForm()
		return render(request, 'blog/post_list1.html', {'form': form})
#	if request.POST:
#		title=request.POST['title']
#		content=request.POST['cont']
#		model_name=request.POST['name']
#		created_data=request.POST['time']
#		mysearch.objects.create(author=me,title=title,content=content,model_name=model_name,created_data=created_data)
#	posts = mysearch.objects.all()
#	return render(request,'blog/post_list1.html',{'posts':posts})