# from django.shortcuts import render, redirect
# from .models import Product
# from django.contrib.auth import login, logout, authenticate
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .forms import SignUpForm


# def home(request):
#     all_products = Product.objects.all()
#     return render(request, 'index.html', context={'products': all_products})


# def about(request):
#     return render(request, 'about.html')


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'با موفقیت وارد شدید')
#             return redirect('home')
#         else:
#             messages.success(request, 'مشکلی در ورود شما وجود دارد')
#     else:
#         return render(request, 'login.html')


# def logout_user(request):
#     logout(request)
#     messages.success(request, "با موفقیت خارج شدید!")
#     return redirect("home")


# def product(request, pk):
#     product = Product.objects.get(pk=pk)
#     return render(request, "product.html", {"product": product})


# def signup_user(request):
#     form = SignUpForm()
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid:
#             form.save()
#             username = form.cleaned_data['username']
#             password1 = form.cleaned_data['password1']
#             user = authenticate(request, username=username, password=password1)
#             login(request, user)
#             messages.success(request,'اکانت شما با موفقیت ساخته شد')
#             return redirect('home')
#         else:
#             messages.success(request, 'اکانت شما با مشکلی مواجه شد')
#             return redirect('signup')
#     else:
#         return render(request, 'signup.html', context={'form': form})



# from rest_framework import generics, status, mixins
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Product, Category
# from .serializers import ProductSerializer, CategorySeializer
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from customer.serializars import CustomerSerializer



# class ProductList(mixins.ListModelMixin, GenericViewSet):
#     serializer_class = ProductSerializer
#     permission_classes = [AllowAny]
#     serializer_class = ProductSerializer


#     def list(self, request, *args, **kwargs):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
    


# class LogoutViewSet(GenericViewSet):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         request.user.auth_token.delete()
#         return Response({'message': 'you are logout successfully.'}, status=status.HTTP_200_OK)
    

# class SignUpViewSet(GenericViewSet):
#     permission_classes = [AllowAny]
#     serializer_classes = [CustomerSerializer]


#     def post(self, request, *args, **kwargs):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             customer = serializer.save()
#             username = serializer.validated_data['username']
#             password = serializer.validate_data['password']
#             customer = authenticate(username=username, password=password)
#             login(request, customer)
#             return Response({'message':'you signup successfully.'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






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
    permission_classes = [IsAuthenticated]


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
            return Response({'token': 'token_key'}, status=status.HTTP_200_OK)
        return Response({'message':'Invalid credential.'}, status=status.HTTP_400_BAD_REQUEST)
    



class LogoutViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def create(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message':'You logout successfully.'}, status=status.HTTP_200_OK)