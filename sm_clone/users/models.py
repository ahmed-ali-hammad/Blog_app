from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models.signals import pre_save, post_save



class UserProfile (models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(blank=True,max_length=100)
	city = models.CharField(blank=True,max_length=100)
	country = models.CharField(blank=True,max_length=100)
	phone = models.IntegerField(default=0)
	image = models.ImageField(default='profile.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name} Profile'

	
class EmailBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		UserModel = get_user_model()

		if '@' in username:
			kwargs = {'email': username}
		else:
			kwargs = {'username': username}

		try:
			user = UserModel.objects.get(**kwargs)
		except UserModel.DoesNotExist:
			return None
		else:
			if user.check_password(password):
				return user
		return None

