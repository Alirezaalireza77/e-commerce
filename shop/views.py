from rest_framework import generics, status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product, Category
from .serializers import ProductSerializer, CategorySeializer, SignUpSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class SignUpViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'user was registered successfully.'},
                            status=status.HTTP_201_CREATED
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return Response({'message':'user was not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            token, create = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message':'Invalid credential.'}, status=status.HTTP_400_BAD_REQUEST)
    



class LogoutViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def create(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message':'You logout successfully.'}, status=status.HTTP_204_NO_CONTENT)
    

class ProductListViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
