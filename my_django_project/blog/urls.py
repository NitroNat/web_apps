from django.conf.urls import url 
from blog import views

# all these views are under the "blog" base directory
urlpatterns = [
	url(r'^blog/$', views.test_redirect, name='test_redirect'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)$', views.post_detail, name='post_detail'),
	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^time/$', views.today_is, name='todays_time'),
	url(r'^$', views.index, name='blog_index'),
]