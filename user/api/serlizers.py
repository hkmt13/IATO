from rest_framework import serializers
from django.contrib.auth.models import User

class UserDisplaySerlizer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields="__all__"

#["username","id","first_name","last_name","email","is_staff","is_active","is_superuser"]

class UserLoginSerlizer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=["username","password"]