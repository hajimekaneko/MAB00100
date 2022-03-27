from os import strerror
from rest_framework import fields, viewsets, generics, status, views
from django.shortcuts import get_object_or_404
from main.models import UserProfile
from main.serializers import UserProfileSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters

class UserProfileLoginAPIView(views.APIView):
    def post(self, request, *args, **Kwargs):
        UserProfile_data = get_object_or_404(UserProfile, email=request.data['email'])
        serializer = UserProfileSerializer(instance=UserProfile_data)
        print(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileLogoutAPIView(views.APIView):
    def delete(self, request, *args, **Kwargs):
        print("■VIEW:LOGOUT")
        token = request.headers['x-kbn-token']
        if token is None :
            return Response("許可されていません", status = status.HTTP_403_FORBIDDEN)
        else:
            return Response(status = status.HTTP_204_NO_CONTENT)