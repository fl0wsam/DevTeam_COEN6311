from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken
from .serializers import *
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
            })
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class PasswordAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    model = User

    def post(self, request):
        user = request.user
        if not user.check_password(request.data.get('password')):
            return Response({'message': "Incorrect Password"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': "Success"}, status=status.HTTP_200_OK)

