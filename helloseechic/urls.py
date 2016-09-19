"""helloseechic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import chicfood.views

urlpatterns = [
    url(r'^$', chicfood.views.index, name='index'),
    url(r'^login$', chicfood.views.loginpage, name='loginpage'),
    url(r'^logout$', chicfood.views.logoutpage, name='logoutpage'),
    url(r'^add$', chicfood.views.addfood, name='addfood'),
    url(r'^search$', chicfood.views.searchpage, name='searchpage'),
    url(r'^admin/', admin.site.urls),
]
