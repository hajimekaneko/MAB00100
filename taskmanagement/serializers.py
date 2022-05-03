from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import List, Task, TaskGroup, TaskStatus
from main.models import UserProfile
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedCreateMixin
from main.serializers import UserProfileSerializer


# class TaskGroupNoSerializerField(serializers.SlugRelatedField):
#     def get_queryset(self):
#         queryset = self.queryset
#         if hasattr(self.root, 'project_id'):
#             queryset = queryset.filter(project_id=project_id)
#         return queryset


class TaskGroupSerializer(WritableNestedModelSerializer):
    User = UserProfileSerializer() 
    Task = SerializerMethodField()
    class Meta:
        model = TaskGroup
        fields = ('User', 'TaskGroupId', 'TaskGroup_sortId','TaskGroup_name', 'TaskGroup_status', 'TaskGroup_created_at', 'TaskGroup_updated_at', 'Task')

    
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
        # depth = 1
        
    # def update(self, validated_date):
    #     print("■■validated_date")
    #     print(validated_date)

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

    Task = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(),
        write_only = True
    )
    List_status = serializers.SlugRelatedField(
        # read_only=False,
        many=False,
        slug_field='TaskStatus_No',
        queryset=TaskStatus.objects.all()
        )
    class Meta:
        model = List
        partial=True
        # fields = '__all__'
        fields = ('Task','ListId', 'List_sortId','List_name', 'List_status', 'List_memo', 'List_created_at', 'List_updated_at')

    print("■")
    # def update(self, validated_date):
    #     print("■■validated_date")
    #     print(validated_date)

    
    # def create(self, validated_date):
    #     validated_date['Task'] = validated_date.get('Task_Id', None)

    #     if validated_date['Task'] is None:
    #         raise serializers.ValidationError("Task not found.") 

    #     del validated_date['Task_Id']

    #     return List.objects.create(**validated_date)