# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib import admin
from django.db import models


class Media(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	media_type = models.CharField(max_length=100)
	file = models.FileField()
	description = models.TextField()

	def __str__(self):
		return "video - " + str(self.pk) + " - " + self.description

class Comment(models.Model):
	media = models.ForeignKey('Media')
	pub_date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	author = models.CharField(max_length=50)

	def __str__(self):
		return "comment on video " + str(self.media.pk) + " - " + self.content[0:20]

admin.site.register(Media)
admin.site.register(Comment)