from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers  import make_password,check_password

# Create your views here.

def index(request):
    return render(request,'index.html')

@api_view(['POST'])
def register_user(request):
    data = request.data
    username = data['username']
    email = data['email']
    password = data['password']
    confirmPassword = data['confirmPassword']
    if password != confirmPassword:
        return Response({'msg':"password and confirm password doesn't match...!"},status=status.HTTP_401_UNAUTHORIZED)    
    else:
        userAdd = User.objects.create(
            username=username,
            email=email,
            password= make_password(password),
        )
    return Response({'msg':"Successfully Register User!!!"},status=status.HTTP_200_OK)

@api_view(['POST'])
def login_user(request):
    data = request.data
    email = data['email']
    password = data['password']
    userList = User.objects.filter(email=email).first()
    if check_password(password,userList.password):
        token, _ = Token.objects.get_or_create(user=userList)
        return Response({'msg':"Successfully Register User!!!",'token': token.key},status=status.HTTP_200_OK)
    return Response({'msg':"username or password doesn't match...!"},status=status.HTTP_401_UNAUTHORIZED)    