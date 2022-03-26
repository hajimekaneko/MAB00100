from os import strerror
from rest_framework import fields, viewsets, generics, status, views
from django.shortcuts import get_object_or_404
from main.models import Auth
from main.serializers import AuthSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters


class Authfilter(filters.FilterSet):
    # フィルタの定義
    emailfilter = filters.CharFilter(name="email", lookup_expr='exact')

    class Meta:
        model = Auth
        fields = '__all__'

class AuthLoginAPIView(views.APIView):
    def post(self, request, *args, **Kwargs):
        auth_data=get_object_or_404(Auth, email=request.data['email'])
        serializer = AuthSerializer(instance=auth_data)
        print(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED)

class AuthViewSet(viewsets.ModelViewSet):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer

class AuthLogoutAPIView(views.APIView):
    def delete(self, request,*args, **Kwargs):
        print("■VIEW:LOGOUT")
        token = request.headers['x-kbn-token']
        if token is None :
            return Response("許可されていません", status = status.HTTP_403_FORBIDDEN)
        else:
            return Response(status = status.HTTP_204_NO_CONTENT)
