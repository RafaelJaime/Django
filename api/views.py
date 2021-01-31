from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from xml.etree.ElementTree import ParseError
from rest_framework.authtoken.models import Token

from account.models import User
from .serializer import ClientSerializer

# Create your views here.
class Users_APIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None, *args, **kwargs):
        clients = User.objects.filter(is_client=True)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
class Users_APIView_Detail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesnNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        if user.is_client:
            serializer = ClientSerializer(user)
            return Response(serializer.data)
        else:
            return Response("No Tienes permisos", status=status.HTTP_401_UNAUTHORIZED)
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ClientSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class TestView(APIView):
    def get(self, request, format=None):
        return Response({'detail': "GET Response"})
    def post(self, request, format=None):
        try:
            data = request.data
        except ParseError as error:
            return Response('Invaled JSON - {0}'.format(error.detail), status=status.HTTP_404_NOT_FOUND)
        if "user" not in data or "password" not in data:
            return Response('Wrong credentials', status = status.HTTP_401_UNAUTHORIZED)
        
        user = authenticate(username=data["user"], password=data["password"])
        if not user:
            return Response('No default user, pleas create one', status=status.HTTP_404_NOT_FOUND)
        if user.is_superuser:
            token = Token.objects.get_or_create(user=user)
            return Response({'detail':'POST answer', 'token':token[0].key})
        else:
            return Response('Not enought permisson, just superuser can get this information', status = status.HTTP_401_UNAUTHORIZED)