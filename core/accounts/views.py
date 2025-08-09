from django.shortcuts import render

# Create your views here.
# account/views.py
from rest_framework import generics, permissions
from .models import MyUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

# Register view
class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# View current user profile
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class LoginView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                return Response({'msg: ''Login Success'},status=status.HTTP_200_OK ) 
            else :
                return Response({'msg: ''Invalid Email or Password'},status=status.HTTP_404_NOT_FOUND)

