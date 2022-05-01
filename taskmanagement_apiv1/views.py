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

# class GetListAPIView(views.APIView):
#     def get(self, request, *args, **Kwargs):

#         # token = request.headers['x-kbn-token']
#         # if token is None :
#         #     return Response("許可されていません", status = status.HTTP_403_FORBIDDEN)
#         # else:
#         #     print("■{}".format(board["lists"]))
#         #     # list = List.objects.all()
#         #     list = get_object_or_404(List) 
#         #     print(list)
#         #     serializer = ListSerializer(instance=list)   
#         #     print("■{}".format(serializer.data))
#             return Response(serializer.data, status = status.HTTP_200_OK)