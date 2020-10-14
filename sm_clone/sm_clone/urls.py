from django.contrib import admin
from django.urls import path, include
from posts import views as posts_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', posts_views.create_post, name='homepage'),
    path('',include('users.urls')),
    path('', include('posts.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
