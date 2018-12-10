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
@csrf_exempt
def post_list(request):
	form=PostForm()
	return render(request,'blog/post_list.html',{'form':form})

@csrf_exempt
def post_list1(request):
	if request.method=="POST":
		title = request.POST[title'].encode('utf-8')
		content = request.POST['content'].encode('utf-8')
		model_name = request.POST['model_name'].encode('utf-8')
#			created_data = form['created_data']
		print (model_name)
		mysearch.objects.create(title = title, content = content, model_name = model_name)
#			form = Comment (title=title,content=content,model_name=model_name,created_data=created_data)
#			form.save()
	form=PostForm()
	return redirect('/blog/')
#	return redirect(request, 'blog/post_list1.html',{'form': form},context_instance=RequestContext(request))
#	if request.POST:
#		title=request.POST['title']
#		content=request.POST['cont']
#		model_name=request.POST['name']
#		created_data=request.POST['time']
#		mysearch.objects.create(author=me,title=title,content=content,model_name=model_name,created_data=created_data)
#	posts = mysearch.objects.all()
#	return render(request,'blog/post_list1.html',{'posts':posts})