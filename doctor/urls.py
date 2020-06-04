"""doctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from . import testdb,view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add$',testdb.testdbAdd),
    url(r'^getAll$',testdb.testdbGet),
    url(r'^update$',testdb.testdbUpdate),
    url(r'^del$',testdb.testdbDel),
    url(r'^index$',view.hello),
    url(r'^$',view.login),
    url(r'^login$',testdb.testdbLogin),
    url(r'^savecode$',testdb.testdbSaveCode),
    url(r'^checkcode$',testdb.testdbCheckCode)
]
