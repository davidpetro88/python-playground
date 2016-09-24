from django.conf.urls import url

from www import views

urlpatterns = [
    url(r'^$', views.index, name='blog.index'),
    # url(r'^$', views.index, name='blog.index'),
    # url(r'^$', views.home, name='blog.home')
]