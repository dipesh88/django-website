from django.conf import settings


D = {"MAX_RETRIES":3}


if hasattr(settings,"TASKS_QUEUE"):
    for key,value in getattr(settings,"TASKS_QUEUE"):
        D[key] = value
        
        
MAX_RETRIES = D["MAX_RETRIES"]
