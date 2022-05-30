from rest_framework import viewsets
from cinema.models import *
from cinema.serializer import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class TheatrViewSet(viewsets.ModelViewSet):
    queryset = Theatr.objects.all()
    serializer_class = TheatrSerializer


class SoonViewSet(viewsets.ModelViewSet):
    queryset = Soon.objects.all()
    serializer_class = SoonSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user_id=response.data["id"])
        response.data["token"] = str(token)
        return response


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(buyers=user)


class SeansViewSet(viewsets.ModelViewSet):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class TSeansViewSet(viewsets.ModelViewSet):
    queryset = TSeans.objects.all()
    serializer_class = TSeansSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})