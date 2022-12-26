from django.shortcuts import render

# Create your views here.
from .serializers import MyUserSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import generate_token

class LoginApi(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = MyUser.objects.filter(email=email).first()
        token = generate_token(user.email)
        print(token)
        # if not user.check_password(raw_password=password):
        #     return Response({"status": 400, "message": "Wrong Password"},status=status.HTTP_400_BAD_REQUEST)
        serializer = MyUserSerializer(user)
        return Response({"message": "User logged in successfully","user_info": serializer.data,"token" : token },status=status.HTTP_200_OK,)


# To get Details Of User
class UserApi(APIView):
    def get(self, request, *args, **kargs):
        user = request.user
        serializer = MyUserSerializer(user)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordAPI(APIView):
    def post(self,request,*args, **kwargs) :
        print("Reset Password ")
        pass
        