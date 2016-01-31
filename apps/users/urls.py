from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$',views.UserSettingsView.as_view(),name="user_settings"),
    
    ]