
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import mysearch
from django.utils import timezone

class PostForm(forms.ModelForm):
	class Meta:
		model = mysearch
#		fields = '_all_'
		fields = ('Class', 'title', 'content', 'created_data', 'publish_data', 'file', 'img')