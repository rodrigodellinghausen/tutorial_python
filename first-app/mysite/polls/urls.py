from django.conf.urls import url

from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^especific/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	#url(r'^abc/$', views.abc, name='abcd')
]