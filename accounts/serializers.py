from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = MyUser
        fields = ['id',"email","password", "password2"]
        
    def save(self):
        user = MyUser(email=self.validated_data["email"])
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if (password and password2) and password != password2:
            raise serializers.ValidationError(
                {"password": "password fields does not match"}
            )
        user.set_password(password)
        user.save()
  
class RegisterUserSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = MyUser
        fields = "__all__"
        
    def save(self):
        user = MyUser(email=self.validated_data["email"])
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user

        