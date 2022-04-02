from rest_framework import serializers
from .models import List, Task, TaskGroup
from drf_writable_nested.serializers import WritableNestedModelSerializer
from main.serializers import UserProfileSerializer



class TaskGroupSerializer(WritableNestedModelSerializer):
    User = UserProfileSerializer() 
    class Meta:
        model = TaskGroup
        fields = ('User', 'TaskGroupId', 'TaskGroup_sortId','TaskGroup_name', 'TaskGroup_status', 'TaskGroup_created_at', 'TaskGroup_updated_at')
        # fields = ('taskId', 'name', 'description','created_at')



class TaskSerializer(WritableNestedModelSerializer):
    TaskGroup = TaskGroupSerializer() 
    class Meta:
        model = Task
        fields = ('TaskGroup', 'TaskId', 'Task_sortId','Task_name', 'Task_status', 'Task_description', 'Task_created_at', 'Task_updated_at')


class ListSerializer(serializers.ModelSerializer):
    # 対象のフィールドのSerializerを置き換えると、ListSerializerを使って展開される
    # ManyToManyのように複数の場合は「many=True」をつける
    # contextを設定すると、URLの展開などをしてくれる
    # tasks = TaskSerializer() 

    # task_set = serializers.
    Task = TaskSerializer() 

    class Meta:
        model = List
        # fields = '__all__'
        fields = ('Task', 'ListId', 'List_sortId','List_name', 'List_status', 'List_memo', 'List_created_at', 'List_updated_at')
        depth = 2