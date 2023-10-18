from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateView, RetrieveUpdateAPIView, DestroyAPIView

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


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

class MenuItemView(ListCreateView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView (RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer