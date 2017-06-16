from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.main_page,name='cmp'),
	url(r'[\w]+',views.error),]