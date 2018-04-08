from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^quiz/all/$', views.quiz_list, name='quiz_list'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)', views.quiz, name='quiz'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)', views.quiz_results, name='quiz_results'),

]
