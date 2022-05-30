from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Cinemas', CinemaViewSet)
router.register(r'Theatr', TheatrViewSet)
router.register(r'Soon', SoonViewSet)
router.register(r'Seat', SeatViewSet)
router.register(r'User', UserViewSet)
router.register(r'Ticket', TicketViewSet)
router.register(r'Seans', SeansViewSet)
router.register(r'TSeans', TSeansViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CustomObtainAuthToken.as_view()),
]
