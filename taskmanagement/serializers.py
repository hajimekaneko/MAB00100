from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import List, Task, TaskGroup
from main.models import UserProfile
from drf_writable_nested.serializers import WritableNestedModelSerializer
from main.serializers import UserProfileSerializer



class TaskGroupSerializer(WritableNestedModelSerializer):
    User = UserProfileSerializer() 
    Task = SerializerMethodField()
    class Meta:
        model = TaskGroup
        fields = ('User', 'TaskGroupId', 'TaskGroup_sortId','TaskGroup_name', 'TaskGroup_status', 'TaskGroup_created_at', 'TaskGroup_updated_at', 'Task')
        depth = 1
    
    def get_Task(self, obj):

        try:
            Task_abstruct_contents = TaskSerializer(Task.objects.all().filter(TaskGroup = TaskGroup.objects.get(TaskGroupId=obj.TaskGroupId)), many=True).data
            return Task_abstruct_contents
        except:
            Task_abstruct_contents = None
            return Task_abstruct_contents



class TaskSerializer(WritableNestedModelSerializer):
    List = SerializerMethodField()   
    print("◆◆◆◆◆◆◆◆◆◆◆◆TaskSerializer")
    class Meta:
        model = Task
        # fields = ('TaskGroup', 'TaskId', 'Task_sortId','Task_name', 'Task_status', 'Task_description', 'Task_created_at', 'Task_updated_at')
        fields = ('TaskId', 'Task_sortId','Task_name', 'Task_status', 'Task_description', 'Task_created_at', 'Task_updated_at', 'List')

    def get_List(self, obj):

        try:
            List_abstruct_contents = ListSerializer(List.objects.all().filter(Task = Task.objects.get(TaskId=obj.TaskId)), many=True).data
            return List_abstruct_contents
        except:
            List_abstruct_contents = None
            return List_abstruct_contents



class ListSerializer(serializers.ModelSerializer):
    # 対象のフィールドのSerializerを置き換えると、ListSerializerを使って展開される
    # ManyToManyのように複数の場合は「many=True」をつける
    # contextを設定すると、URLの展開などをしてくれる
    # tasks = TaskSerializer() 

    # task_set = serializers.


    class Meta:
        model = List
        # fields = '__all__'
        fields = ('ListId', 'List_sortId','List_name', 'List_status', 'List_memo', 'List_created_at', 'List_updated_at')
        depth = 1