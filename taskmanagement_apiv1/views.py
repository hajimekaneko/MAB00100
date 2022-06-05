from os import strerror
from rest_framework import fields, viewsets, generics, status, views
from django.shortcuts import get_object_or_404
from taskmanagement.models import List, Task, TaskGroup
from taskmanagement.serializers import ListSerializer, TaskSerializer, TaskGroupSerializer
from rest_framework.response import Response

class TaskGroupViewSet(viewsets.ModelViewSet):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class FetchListAPIView(views.APIView):
    def get(self, request, *args, **Kwargs):
        queryset = TaskGroup.objects.filter(User=self.request.query_params.get('UserId'))
        serializer = TaskGroupSerializer(instance=queryset, many=True)         
        return Response(serializer.data, status = status.HTTP_200_OK)
