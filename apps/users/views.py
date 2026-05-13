from rest_framework import generics
from apps.users.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 
    
class ProfileView(RetrieveAPIView):
    def get_object(self):
        return self.request.user
    serializer_class = UserSerializer