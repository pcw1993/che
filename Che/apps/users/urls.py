# -*- coding:utf-8 -*-

# author: pcw
# datatime: 2018/11/23 9:41 AM
# software: PyCharm

from django.conf.urls import url, include
from django.contrib import admin


from users import views

urlpatterns = [
    # url(r'^register$', views.register)
    # 访问类视图，使用as_view方法转换类视图
    url(r'^register$', views.RegisterView.as_view(), name='register'),  # 反向解析
    # url(r'^active/(?P<token>.+)$', views.ActiveView.as_view(), name='active'),  # 反向解析
    # url(r'^login$', views.LoginView.as_view(), name='login'),  # 反向解析
    # url(r'^logout$', views.LogoutView.as_view(), name='logout'),  # 反向解析
    # url(r'^address$', views.AddressView.as_view(), name='address'),  # 反向解析
    # url(r'^info$', views.UserInfoView.as_view(), name='info'),  # 反向解析
]