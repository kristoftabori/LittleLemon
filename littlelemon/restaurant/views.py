from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer

def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):

    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})


# class MenuView(APIView):

#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuSerializer(items, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView (RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]