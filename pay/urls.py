from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'pay'
urlpatterns = [
        url(r'^index/$', views.index , name = 'index'),
        url(r'^home/$', views.home , name = 'home'),
        url(r'^test/$', views.test , name = 'test'),
        url(r'^Transaction/$', views.Transactioning , name = 'Transactioning'),
        url(r'^Transaction1/$', views.Transaction1 , name = 'Transaction1'),
        url(r'^Transaction2/$', views.Transaction2 , name = 'Transaction2'),
        url(r'^Transaction3/$', views.Transaction3 , name = 'Transaction3'),
        url(r'^Transaction4/$', views.Transaction4 , name = 'Transaction4'),
        url(r'^feedback/$', views.feedback , name = 'feedback'),
        url(r'^coupons/$', views.Coupon , name = 'Coupon'),
        url(r'^complaint/$', views.complaint , name = 'complaint'),
        url(r'^detail/(?P<id>\d+)$', views.detail , name = 'detail'),
        url(r'^Block/(?P<id>\d+)$', views.Block , name = 'Block'),
        url(r'^UnBlock/(?P<id>\d+)$', views.UnBlock , name = 'UnBlock'),
        url(r'^delete/(?P<id>\d+)$', views.delete , name = 'delete'),
        url(r'^update/(?P<id>\d+)$', views.update , name = 'update'),
        url(r'^Serviced1/$', views.Serviced1 , name = 'Serviced1'),
        url(r'^Serviced2/$', views.Serviced2 , name = 'Serviced2'),
        url(r'^Serviced3/$', views.Serviced3 , name = 'Serviced3'),
        url(r'^Serviced4/$', views.Serviced4 , name = 'Serviced4'),
        url(r'^Serviced5/$', views.Serviced5 , name = 'Serviced5'),
        url(r'^Serviced6/$', views.Serviced6 , name = 'Serviced6'),
        ]
