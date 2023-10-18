from django.urls import path 
from . import views
  
urlpatterns = [ 
    # path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('booking/', views.BookingView.as_view()),
]