from django.urls import path
from . import views 

urlpatterns = [

	path("create/post/", views.create_post , name ='create_post'),
	path("update/post/<slug:slug>/", views.PostUpdateView.as_view(), name = 'post_update'),
	path("delete/post/<slug:slug>/", views.PostDeleteView.as_view(), name = 'post_delete'),
	path("<slug:slug>/", views.post_details, name = 'post_details'),
	
]
