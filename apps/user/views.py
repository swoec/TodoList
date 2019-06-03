# Create your views here.


from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import UserProfile
from .serializers import UserSerializer, UserEmailSerializer, UserAddSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


# User = get_user_model()


# Create your views here.

class CustomBackend(ModelBackend):
    """
    user verification
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class UserViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserEmailSerializer


class UseraddViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAddSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):

        return serializer.save()
