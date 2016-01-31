"""site_repo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static

from home.views import home_page
from apps.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_page, name='hello-world'),
    url(r'^sign-up/$', auth_views.SignUpView.as_view(), name='sign_up_simple'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login_simple'),
    url(r'^logout/$', auth_views.logout_user, name='logout_simple'),
    
    url(r'^settings/', include('site_repo.apps.users.urls',namespace='users')),
    url(r'^expenses/', include('site_repo.apps.expenses.urls',namespace='expenses')),
    url(r'^balance/', include('site_repo.apps.balance.urls',namespace='balance')),
]

if settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$', views.serve),]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    
    
