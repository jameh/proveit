from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^login/$',  login, {'template_name': 'proveit/login.html'}),
    (r'^logout/$', logout, {'template_name': 'proveit/logout.html', 'next_page': '/'}),
    url(r'^signup$', views.register, name='register'),
    url(r'^new$', views.new, name='new'),
    url(r'^([a-zA-Z0-9]+)/edit$', views.edit, name='edit'),
    # url(r'^proofs$', view.proo)
)
