from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns =[
	url(r'^$', views.index, name='index'),
	url(r'media/([0-9]+)/view$', views.media_detail, name='media_detail'),
	url(r'media/upload$', views.upload_media, name='upload_media'),
	url(r'media/([0-9]+)/post-comment$', views.post_comment, name='post_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)