from django.shortcuts import render

from django.views import generic


class UserSettingsView(generic.TemplateView):
    
    template_name = "users/user_settings.html"
