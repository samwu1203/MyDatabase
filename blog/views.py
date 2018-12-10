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
import os, sys
import json
@csrf_exempt
def post_list(request):
	form=PostForm()
	return render(request,'blog/post_list.html',{'form':form})

@csrf_exempt
def post_list1(request):
	if request.method=="POST":
		data=request.body
		data=data.split('\r\n')
		title=str(data[1]).split('=')[1]
		content=str(data[2]).split('=')[1]
		model_name=str(data[3]).split('=')[1]
		POST = {'title': title,
				'content': content,
				'model_name': model_name,}
		form = PostForm(POST)
		if form.is_valid():
			form.save()
			form = PostForm()
			posts = mysearch.objects.all()
			return render(request, 'blog/post_list.html',{'form':form, 'posts':posts})
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
		return render(request, 'blog/post_list1.html', {'form': form}, {'posts':posts})
#	if request.POST:
#		title=request.POST['title']
#		content=request.POST['cont']
#		model_name=request.POST['name']
#		created_data=request.POST['time']
#		mysearch.objects.create(author=me,title=title,content=content,model_name=model_name,created_data=created_data)
#	posts = mysearch.objects.all()
#	return render(request,'blog/post_list1.html',{'posts':posts})