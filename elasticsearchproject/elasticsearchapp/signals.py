# from .models import BlogPost
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=BlogPost)
def index_post(sender, instance, **kwargs):
	# import ipdb; ipdb.set_trace()
	instance.indexing()

# @receiver(pre_save, sender=BlogPost)
# def index_post(sender, instance, **kwargs):
# 	import ipdb; ipdb.set_trace()
# 	instance.indexing()