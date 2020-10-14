from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.urls import reverse



class Posts(models.Model):
	title = models.CharField(max_length=100)
	slug = models.CharField(max_length=100, blank = True)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	thumbnail = models.ImageField(default= 'default.png', blank = True)


	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_details', kwargs = {"slug": self.slug})

		
def slug_genertor(instance, sender, *args, **kwargs):
	slug_dic = instance.title.lower().split(' ')
	instance.slug = slug_dic[0] + '-'+ slug_dic[-1]

pre_save.connect(slug_genertor, sender = Posts)

	


