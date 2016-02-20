import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"   
    
import django

def set_env():
    """ load django, and set site specific environment"""
    django.setup()