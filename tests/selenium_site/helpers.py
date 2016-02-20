import django

def set_env():
    """ load django, and set site specific environment"""
    django.setup()