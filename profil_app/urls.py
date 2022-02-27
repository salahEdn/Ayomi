from django.urls import re_path, include
from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    re_path(r'^users/$', views.users_list, name='users_list'),
    re_path(r'^users/(?P<id>\d+)/update$', views.users_update, name='users_update'),
]
