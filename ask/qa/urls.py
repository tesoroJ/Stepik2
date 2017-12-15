from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='test'),
    url(r'^login/', views.test, name='test'),
    url(r'^signup/', views.test, name='test'),
    url(r'^question/(?P<pk>\d+)/$', views.question, name='question_text'),
    url(r'^ask/', views.test, name='test'),
    url(r'^popular/', views.popular, name='test'),
    url(r'^new/', views.test, name='test'),
]