from django import forms

class MediaUploadForm(forms.Form):
    file = forms.FileField()
    description = forms.CharField(max_length=280)

class CommentForm(forms.Form):
	author = forms.CharField(label='Name', max_length=100)
	content = forms.CharField(widget=forms.Textarea)