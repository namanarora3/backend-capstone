from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegisterUser(APIView):

  def post(self, request):
    data = request.data
    serializer = RegisterUserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response({"status":"success", "data":serializer.data}, status=status.HTTP_201_CREATED)

class LoginUser(APIView):

  def post(self, request):
    data = request.data
    # CustomUser.objects.get(email=data.get('email'))
    serializer = LoginUserSerializer(data=data)
    if serializer.is_valid():
      user = serializer.validated_data['user']
      admin = user.is_official
      token,_ = Token.objects.get_or_create(user=user)
      return Response({"Status":"Success", "Token":str(token), 'email':serializer.validated_data['email'], 'admin':admin}, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ValidationError
from .models import CustomUser
from .serializers import UserSerializer

class UserDetails(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return CustomUser.objects.get(id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if 'email' in request.data and CustomUser.objects.filter(email=request.data['email']).exclude(id=user.id).exists():
            return Response({'error':'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)