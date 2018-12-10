
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import mysearch

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=200)
	content = forms.CharField(max_length=200)
	model_name = forms.CharField(max_length=200)
	class Meta:
		model = mysearch
#		fields = '_all_'
		fields = ('title', 'content', 'model_name')