from django.contrib.auth.models import User
from django.conf import settings

class EmailAuth(object):
    
    def get_user(self,user_id):
        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
            
    
    def authenticate(self,username,password):
        
        if settings.DEBUG and settings.DEBUG_ALLOW_NON_UNIQUE_EMAIL:
            queryset = User.objects.filter(email=username).first()            
        else: 
            queryset = User.objects.get(email=username)
             
        try:
            user =  queryset
            if user.is_active and user.check_password(password):
                return user
            else:
                return None
        except:
            return None
            
             
             
        
        
        