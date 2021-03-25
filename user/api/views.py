
from rest_framework import generics;
from .serlizers import UserDisplaySerlizer,UserLoginSerlizer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class CurrentUserAPIView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserDisplaySerlizer
  #  permission_classes= (IsAuthenticated,)


class LoginUser(generics.ListCreateAPIView):
    serializer_class=UserLoginSerlizer
    def get_queryset(self, request):
        user = authenticate(username=self.request.username,password=self.request.password)
        if user is not None:
            print(user);
            token = Token.objects.create(user=self.request.user);
            print (token.key);
            return
        # A backend authenticated the credentials
        else: print("fsf");



    