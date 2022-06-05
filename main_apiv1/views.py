from os import strerror
from sqlite3 import adapters
from rest_framework import fields, viewsets, generics, status, views
from django.shortcuts import get_object_or_404
from main.models import UserProfile
from main.serializers import UserProfileSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from firebase_admin import auth


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views  import SocialLoginView


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    cliant_class = OAuth2Client


class UserProfileLoginAPIView(views.APIView):
    def post(self, request, *args, **Kwargs):
        print(request.data)
        decoded_token = auth.verify_id_token(request.data)
        uid = decoded_token['uid']
        print(uid)

        user_profile_data = get_object_or_404(UserProfile, userId=uid)
        print(user_profile_data)
        serializer = UserProfileSerializer(instance=user_profile_data)
        user_profile_data.loggedin = True
        user_profile_data.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class UserProfileSignupAPIView(views.APIView):
    def post(self, request, *args, **Kwargs):
        print(request.data)
        decoded_token = auth.verify_id_token(request.data)
        uid = decoded_token['uid']
        print(uid)
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # user_profile_data = get_object_or_404(UserProfile, userId=uid)
        # print(user_profile_data)
        # 
        # user_profile_data.loggedin = True
        # user_profile_data.save()
        # return Response(serializer.errors, status.HTTP_201_CREATED)
        

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileLogoutAPIView(views.APIView):
    def delete(self, request, *args, **Kwargs):
        token = request.headers['x-kbn-token']
        if token is None :
            return Response("許可されていません", status = status.HTTP_403_FORBIDDEN)
        else:
            return Response(status = status.HTTP_204_NO_CONTENT)