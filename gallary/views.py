from django.forms import ValidationError
from accounts.serializers import RegisterUserSerializer
from .serializers import *
from .models import *
from BMS.GM import GenericMethodsMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.services import generate_token
import os


class MakeUpArtistDetailView(GenericMethodsMixin, APIView):
      model = MakeUpArtist
      serializer_class = MakeUpArtistSerializer
      lookup_field = "id"

      def post(self,request,*args, **kwargs):
            serializer = MakeUpArtistSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer = MakeUpArtistSerializer(data=request.data)
                  if serializer.is_valid(raise_exception=True) : 
                        serializer.save()
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                  return Response({"message" : "User Not Found"},status=status.HTTP_400_BAD_REQUEST)
        

class LoginApi(APIView):
    def post(self, request):
        print(request.data)
        email = request.data["email"]
        password = request.data["password"]
        user = MakeUpArtist.objects.filter(email=email).first()
        print(user)
        if user is None : 
            return Response({"data" : "User Not Exists"},status=status.HTTP_404_NOT_FOUND)
        print(user.password,password)
        token = generate_token(user.email)
        print(token)

     
        # if not user.check_password(raw_password=password):
        #     return Response({"status": 400, "message": "Wrong Password"},status=status.HTTP_400_BAD_REQUEST)
        serializer = MakeUpArtistSerializer(user)

        data = {"message": "User logged in successfully","user_info": serializer.data,"token" : token}
        print(data)
        return Response(data,status=status.HTTP_200_OK,)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

      
class NormalImageAPI(GenericMethodsMixin, APIView):
      model = NormalImage
      serializer_class = NormalImageSerializer
      lookup_field = "id"


class BAImageAPI(GenericMethodsMixin,APIView):
      model = BAImage
      seriallizer_class = BASerializer
      lookup_field = "id"

class CatagoryImageAPI(GenericMethodsMixin,APIView):
      model = CatagoryImage
      serializer_class = CatagoryImageSerializer
      lookup_field = "id"