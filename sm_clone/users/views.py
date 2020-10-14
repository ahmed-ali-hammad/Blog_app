from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts import models as posts_models
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterationForm, UserAuthenticationForm, UserUpdateForm, UserProfileUpdateForm
from posts.forms import CreatePostForm 

def register(request):
	if request.method =='POST':
		form_1 = UserRegisterationForm(request.POST)
		form_2 = UserAuthenticationForm(data = request.POST)
		if form_1.is_valid():
			username = form_1.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			user = form_1.save()
			login (request, user)
			return redirect('homepage')
		elif form_2.is_valid():
			user = form_2.get_user()
			login (request , user)
			if 'next' in request.POST:
				return redirect (request.POST.get('next'))
			return redirect ('homepage')
	else:
		form_1 = UserRegisterationForm()
		form_2 = UserAuthenticationForm()
	if 'password2' in request.POST:
		form_2 = UserAuthenticationForm()
		return render (request, 'users/register.html', {'form_1':form_1, 'form_2':form_2})
	else:
		form_1 = UserRegisterationForm()
		return render (request, 'users/register.html', {'form_1':form_1, 'form_2':form_2})

def login_view(request):
	if request.method =='POST':
		form_1 = UserRegisterationForm(request.POST)
		form_2 = UserAuthenticationForm(data = request.POST)
		if form_1.is_valid():
			first_name = form_1.cleaned_data.get('first_name')
			last_name = form_1.cleaned_data.get('last_name')
			messages.success(request, f'Account created for {first_name} {last_name}!')
			user = form_1.save()
			login (request, user)
			return redirect('homepage')
		elif form_2.is_valid():
			user = form_2.get_user()
			login (request , user)
			if 'next' in request.POST:
				return redirect (request.POST.get('next'))
			return redirect ('homepage')
	else:
		form_1 = UserRegisterationForm()
		form_2 = UserAuthenticationForm()
	if 'password2' in request.POST:
		form_2 = UserAuthenticationForm()
		return render (request, 'users/login.html', {'form_1':form_1, 'form_2':form_2})
	else:
		form_1 = UserRegisterationForm()
		return render (request, 'users/login.html', {'form_1':form_1, 'form_2':form_2})



@login_required
def view_profile(request):
	posts = posts_models.Posts.objects.filter(author = request.user)
	if request.method == 'POST':
		form = CreatePostForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()
			form = CreatePostForm()
			return render (request, 'users/view_profile.html', {'form': form, 'posts': posts})
	else:
		form = CreatePostForm()
	return render (request, 'users/view_profile.html', {'user': request.user, 'posts': posts, 'form':form})

@login_required
def edit_profile(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		up_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
		if u_form.is_valid() and up_form.is_valid():
			u_form.save()
			up_form.save()
			return redirect('view_profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		up_form = UserProfileUpdateForm(instance=request.user.userprofile)

	return render (request, 'users/edit_profile.html', {'u_form':u_form, 'up_form':up_form})