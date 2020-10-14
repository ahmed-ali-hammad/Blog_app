from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .models import UserProfile


def username_genertor(instance, sender, *args, **kwargs):
	if not instance.username:
		instance.username = instance.first_name +'_'+ instance.last_name 
		

pre_save.connect(username_genertor, sender = User)
	

def create_UserProfile(instance, sender, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_UserProfile, sender = User)

