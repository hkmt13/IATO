from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserDisplaySerlizer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["username","id","first_name","last_name","email","is_staff","is_active","is_superuser"]



class UserLoginSerlizer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=["username","password"]