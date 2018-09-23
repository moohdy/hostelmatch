#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



class Phone_numberAuthBackend(object):
    """
    authenticate/  user via registered unique phone number.
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(phone_number=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None