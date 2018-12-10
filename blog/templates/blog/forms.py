
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import forms

class PostForm(forms.Form):
	title=forms.CharField(max_length=100)
	content=forms.CharField(max_length=2000,widget=forms.Textarea())
	model_name=forms.CharField(max_length=100)
	created_data=forms.CharField(max_length=100)