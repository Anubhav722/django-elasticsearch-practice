# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from .signals import indexpost
from .search import BlogPostIndex
# Create your models here.

class BlogPost(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
	posted_date = models.DateField(default=timezone.now())
	title = models.CharField(max_length=200)
	text = models.TextField(max_length=1000)

	def __unicode__(self):
		return self.title

	def indexing(self):
		obj = BlogPostIndex(
			meta = {'id': self.id},
			author = self.author.username,
			posted_date = self.posted_date,
			title = self.title,
			text = self.text	
			)
		obj.save()
		return obj.to_dict(include_meta=True)

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=BlogPost)
def index_post(sender, instance, **kwargs):
	# import ipdb; ipdb.set_trace()
	instance.indexing()