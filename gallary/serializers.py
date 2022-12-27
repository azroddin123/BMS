from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import * 

class MakeUpArtistSerializer(serializers.ModelSerializer):
    class Meta :
        model  = MakeUpArtist
        fields = "__all__"

class NormalImageSerializer(serializers.ModelSerializer):
    class Meta :
        model = NormalImage
        fields = "__all__"

class BASerializer(serializers.ModelSerializer):
    class Meta :
        model = BAImage
        fields = "__all__"

class CatagoryImageSerializer(serializers.ModelSerializer):
    class Meta :
        model = CatagoryImage
        fields = "__all__"

