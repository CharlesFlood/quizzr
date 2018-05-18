from django.conf.urls import url

from . import views

app_name = 'security_quiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^quiz/all/$', views.quiz_list, name='quiz_list'),
    url(r'^quiz/(?P<quiz_num>[0-9]+)', views.take_quiz, name='take_quiz'),
    url(r'^quiz/(?P<quiz_num>[0-9]+)', views.quiz_results, name='quiz_results'),

]
