# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import chain
from operator import attrgetter

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import MediaUploadForm, CommentForm
from .models import Media, Comment

def index(request):
	media_activity = Media.objects.all().order_by('-pub_date')
	comment_activity = Comment.objects.all().order_by('-pub_date')
	activity = sorted(chain(media_activity, comment_activity), key=attrgetter('pub_date'))
	activity.reverse()
	activities = []
	for event in activity:
		if event.__class__.__name__ == 'Comment':
			activities.append({'comment':True, 'author': event.author, 'pk': event.media.pk, 'pub_time': event.pub_date.time})
		elif event.__class__.__name__ == 'Media':
			activities.append({'video':True, 'author': 'Somebody', 'pk': event.pk, 'pub_time': event.pub_date.time})

	return render(request, 'video_share/index.html', {'activity': activities})

def media_detail(request, pk):
	media_object = Media.objects.get(pk=pk)
	comments = Comment.objects.filter(media=media_object).order_by('pub_date')
	context = {'file': media_object.file, 'description': media_object.description, 'form': CommentForm, 'comments': comments}
	return render(request, 'video_share/media_detail.html', context)

def upload_media(request):
	if request.method == 'POST':
		form = MediaUploadForm(request.POST, request.FILES)

		if form.is_valid():
			print "form is valid"
			media_record = Media(**form.cleaned_data)
			media_record.save()
			return HttpResponseRedirect('/')
	else:
		form = MediaUploadForm()

	return render(request, 'video_share/upload_media.html', {'form': form})

def post_comment(request, pk):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment_record = Comment.objects.create(media=Media.objects.get(pk=pk), **form.cleaned_data)
			comment_record.save()
			return HttpResponseRedirect('media/'+ pk +'/view')
	else:
		form = CommentForm()

	return render(request, 'video_share/post_comment.html', {'form': form, 'pk': pk})


def solo_live(request):
	return render(request, 'video_share/solo_live.html')