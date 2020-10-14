from django import forms
from . import models

class CreatePostForm(forms.ModelForm):
	class Meta:
		model = models.Posts
		fields = ['title' , 'body', 'thumbnail']
		comment = forms.CharField(widget=forms.TextInput)