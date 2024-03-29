from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from userAuth.serializers import UserRegistrationSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class TokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration Success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)