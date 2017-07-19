from django.conf.urls import url
from django.contrib.auth.views import *
from . import views
urlpatterns = [
	#Previous Login Views
	#url(r'^login/$',views.user_login,name='login'),

	#Login and Logout URLs :)
	url(r'^login/$',login,name='login'),
	url(r'^logout/$',logout,name='logout'),
	url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),
	url(r'^$',views.dashboard, name='dashboard'),	
	#Password Change URLs
	url(r'^password-change/$',password_change,name="password_change"),
	url(r'^password-change/done/$',password_change_done,name="password_change_done"),
	#Reset Password URLs
	url(r'^password-reset/$',password_reset,name='password_reset'),
	url(r'^password-reset/done/$',password_reset_done,name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,name='password_reset_confirm'),
	url(r'^password-reset/complete/$',password_reset_complete,name='password_reset_complete'),
	#New User Registration URLs
	url(r'^register/$', views.register,name='register'),
	#User Profile Edit
	url(r'^edit/$',views.edit,name='edit'),
]