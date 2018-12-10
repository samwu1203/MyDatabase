#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import mysearch
import os, sys
@csrf_exempt
def post_list(request):
	return render(request,'blog/post_list.html',{})

@csrf_exempt
def post_list1(request):
	mysearch.objects.create(title=request.GET['title'],content=request.GET['cont'],model_name=request.GET['name'],created_data=request.GET['time'])
	posts = mysearch.objects.all()
	return render(request,'blog/post_list1.html',{'posts':posts})

def add_record(request):
	
	list=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None];
	dist = 0

	if ('info1' in request.GET):
		list[0] = Busstation.objects.all()

	if ('info2' in request.GET):
		list[1] = Mrtstation.objects.all()

	if ('info3' in request.GET):
		list[2] = Park.objects.all()
	
	if ('info4' in request.GET):
		list[3] = Gost.objects.all()

	if ('info5' in request.GET):
		list[4] = Sensual.objects.all()
	
	if ('info6' in request.GET):
		list[5] = Undertaker.objects.all
	
	if ('info7' in request.GET):
		list[6] = Baby.objects.all()
	
	if ('info8' in request.GET):
		list[7] = School.objects.all()
	
	if ('info9' in request.GET):
		list[8] = Library.objects.all()
	
	if ('info10' in request.GET):
		list[9] = Market.objects.all()
	
	if ('info11' in request.GET):
		list[10] = Temple.objects.all()
	
	if ('info12' in request.GET):
		list[11] = Carburg.objects.all()
		
	if ('info13' in request.GET):
		list[12] = Houseurg.objects.all()
		
	if ('info14' in request.GET):
		list[13] = Accide.objects.all()
	
	if ('info15' in request.GET):
		list[14] = Alley.objects.all()
	
	# if ('info16' in request.GET):
		# list[15] = Ychouse.objects.all()
	
	# if ('info17' in request.GET):
		# list[18] = Highsoil.objects.all().values('lat','lng').distinct()
	
	if ('info20' in request.GET):
		list[19] = Hospital.objects.all()
	
	if ('info24' in request.GET):
		dist = 300
	
	if ('info25' in request.GET):
		dist = 500
		
	if ('info26' in request.GET):
		dist = 1000
	
	address = request.GET['add']
	posts = list[0]
	post1 = list[1]
	post2 = list[2]
	post3 = list[3]
	post4 = list[4]
	post5 = list[5]
	post6 = list[6]
	post7 = list[7]
	post8 = list[8]
	post9 = list[9]
	post10 = list[10]
	post11 = list[11]
	post12 = list[12]
	post13 = list[13]
	post14 = list[14]
	post15 = Ychouse.objects.all()
	post16 = list[16]
	post17 = list[17]
	post18 = Highsoil.objects.all().values('lat','lng').distinct()
	post19 = list[19]
	
	return render(request,'blog/add_record.html',{'posts':posts,'post1':post1,'post2':post2,'post3':post3,\
		'post4':post4,'post5':post5,'post6':post6,'post7':post7,'post8':post8,'post9':post9,'post10':post10,\
		'post11':post11,'post12':post12,'post13':post13,'post14':post14,'post15':post15,'post16':post16,\
		'post17':post17,'post18':post18,'post19':post19,'address':address,'dist':dist})

def add2_record(request):
	
	block=[None,None,None,None,None,None,None];
	check=0
	
	if ('info21' in request.GET):
		block[0] = Undertaker.objects.all()
		check = 1
		
	if ('info22' in request.GET):
		block[1] = Sensual.objects.all()
		check = 2
		
	if ('info23' in request.GET):
		block[2] = Lowsoil.objects.all().values('lat','lng').distinct()
		block[3] = Mediumsoil.objects.all().values('lat','lng').distinct()
		block[4] = Highsoil.objects.all().values('lat','lng').distinct()
		check = 3
	if ('info24' in request.GET):
		block[5] = Houseurg.objects.all()
		check = 4
	if ('info25' in request.GET):
		block[6] = Carburg.objects.all()
		check = 5
	
	post20 = block[0]
	post21 = block[1]
	post22 = block[2]
	post23 = block[3]
	post24 = block[4]
	post25 = block[5]
	post26 = block[6]

	return render(request,'blog/add2_record.html',{'post20':post20,'post21':post21,'post22':post22,'post23':post23,'post24':post24,'post25':post25,'post26':post26,'check':check})

	
def add3_record(request):
	
	address = request.GET['add']
	dist = request.GET['dist']
	post11 = Ychouse.objects.all()
	return render(request,'blog/add3_record.html',{'post11':post11,'address':address,'dist':dist})
	
	
def add4_record(request):
	
#	if ('object' in request.GET):
	str = request.GET['object'].split(",")
	a = str[0]
	b = str[1]
	c = str[2]
	d = str[3]
	post12 = Ychouse.objects.filter(oid__in = [b,c,d])
	post13 = Ychouse.objects.get(oid =a)
	return render(request,'blog/add4_record.html',{'post12':post12,'post13':post13})

# Create your views here.
# return render(request,'blog/add_record.html',{'posts':posts,'post2':post2,'post3':post3 ,'address':address,'dist':dist})