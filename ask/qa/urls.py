from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='test'),
    url(r'^login/', views.test, name='test'),
    url(r'^signup/', views.test, name='test'),
    url(r'^question/(?P<pk>\d+)/$', views.question, name='question_text'),
    url(r'^ask/', views.question_ask, name='test'),
    url(r'^answer/.*$', views.question_ans, name='question_ans'),
    url(r'^popular/', views.popular, name='test'),
    url(r'^new/', views.test, name='test'),
]