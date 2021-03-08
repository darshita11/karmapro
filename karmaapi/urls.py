from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'index/$', views.index.as_view(), name='index'),
    url(r'login/$', views.login_view, name='login'),
    url(r'blog/$', views.blog.as_view(), name='blog'),
    url(r'cart/$', views.cart.as_view(), name='cart'),
    url(r'category/$', views.category.as_view(), name='category'),
    url(r'checkout/$', views.checkout.as_view(), name='checkout'),
    url(r'confirm/$', views.confirm.as_view(), name='confirm'),
    url(r'contact/$', views.contact.as_view(), name='contact'),
    url(r'elements/$', views.elements.as_view(), name='elements'),
    url(r'singleblog/$', views.singleblog.as_view(), name='singleblog'),
    url(r'singleproduct/$', views.singleproduct.as_view(), name='singleproduct'),
    url(r'tracking/$', views.tracking.as_view(), name='tracking'),
    url(r'signup/$', views.signup_view, name='signup'),
]