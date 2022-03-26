from os import strerror
from rest_framework import fields, viewsets, generics, status, views
from rest_framework import response
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404
from main.models import Auth
from main.serializers import AuthSerializer
from taskmanagement.models import List, Task
from taskmanagement.serializers import ListSerializer, TaskSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters

# class AuthLogin(viewsets.ModelViewSet):
#     queryset = Auth.objects.all()
#     serializer = AuthSerializer(queryset, many=True)

# タスクリストID
nextTaskListId = 0
# タスクID
nextTaskId = 0

# タスクリストIDを生成するヘルパー関数
def generateTaskListId():
    global nextTaskListId
    nextTaskListId+=1
    return nextTaskListId

# タスクIDを生成するヘルパー関数
def generateTaskId():
    global nextTaskId
    nextTaskId +=1
    return nextTaskId

# タスクを作成をするヘルパー関数
def createTask(listId):
    task={
        "id": generateTaskId(),
        "name":"タスク" + str(nextTaskId),
        "description":"これはタスク" +str(nextTaskId) + "です",
        "listId":listId
    }
    return(task)


# タスクリストを作成するヘルパー関数
def createTaskList(name, num):
    id = generateTaskListId()   
    list = {
        "listId": id,
        "name": name,
        "items": []
    }
    for i in range(num):
        list["items"].append(createTask(id))
    return list

# ボード情報
board = {
    "lists": [
      createTaskList('TODO', 1),
      createTaskList('WIP', 1),
      createTaskList('DONE', 1)
    ]
  }

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

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class GetListAPIView(views.APIView):
    def get(self, request, *args, **Kwargs):

        # token = request.headers['x-kbn-token']
        # if token is None :
        #     return Response("許可されていません", status = status.HTTP_403_FORBIDDEN)
        # else:
        #     print("■{}".format(board["lists"]))
        #     # list = List.objects.all()
        #     list = get_object_or_404(List) 
        #     print(list)
        #     serializer = ListSerializer(instance=list)   
        #     print("■{}".format(serializer.data))
            return Response(serializer.data, status = status.HTTP_200_OK)