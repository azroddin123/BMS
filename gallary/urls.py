from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    # path('register',RegisterApi.as_view()),
    path('makeup/<int:pk>',MakeUpArtistDetailView.as_view()),
    path('makeup',MakeUpArtistDetailView.as_view()),
    path('login',LoginApi.as_view()),
    path('upload_image',NormalImageAPI.as_view()),
    path('upload_image/<int:pk>',NormalImageAPI.as_view()),
    path('ba_image',BAImageAPI.as_view()),
    path('ba_image/<int:pk>',BAImageAPI.as_view()),
    path('catagory_image',CatagoryImageAPI.as_view()),
    path('catagory_image/<int:pk>',CatagoryImageAPI.as_view())
    ]
