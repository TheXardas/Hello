from django.conf.urls import patterns, include, url
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/card/$', views.card, name='card'),
    url(r'^(?P<poll_id>\d+)/results/$', views.vote_card, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
