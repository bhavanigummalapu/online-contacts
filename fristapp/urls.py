"""telusuko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('student_data_create',views.student_data,name='student_data'),
    path('student_data_delete/(?P<id>\d+)/$',views.student_data_delete,name='student_data_delete'),
    path('student_data_update/(?P<id>\d+)/$', views.student_data_update,name='student_data_update'),
    path('signup',views.user_regisration,name='sign_up'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),



]
