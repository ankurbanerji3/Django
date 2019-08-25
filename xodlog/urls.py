from django.conf.urls import url
from xodlog import views


def as_view():
    pass


urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^sig_log/$', views.detail.as_view(), name='detail'),
    url(r'^sig_sup/$', views.detail1.as_view(), name='detail1'),
    url(r'^sig_log/login/$', views.log, name='log'),
    url(r'^sig_log/signup/$', views.log, name='log'),
    url(r'^board/(?P<user_id>[0-9]+)/$', views.Game_Board.as_view(), name='gameboard'),

]