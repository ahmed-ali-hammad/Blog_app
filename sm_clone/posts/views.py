from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from . import forms


@login_required
def create_post(request):
	articles = models.Posts.objects.all().order_by('date')
	if request.method == 'POST':
		form = forms.CreatePostForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()
			form = forms.CreatePostForm()
			return render (request, 'posts/create_post.html', {'form': form, 'articles':articles})
	else:
		form = forms.CreatePostForm()

	return render (request, 'posts/create_post.html', {'form': form, 'articles':articles})



@login_required
def post_details(request, slug):
	post = models.Posts.objects.get(slug = slug)
	return render (request, 'posts/post_details.html', {'post': post})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = models.Posts
	template_name = 'posts/post_update.html'
	context_object_name = 'post'
	fields = ['title' , 'body', 'thumbnail']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = models.Posts
	template_name = 'posts/post_delete.html'
	context_object_name = 'post'
	success_url = '/'


	def test_func(self):
			post = self.get_object()
			if self.request.user == post.author:
				return True
			return False
