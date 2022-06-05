from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import List, Task, TaskGroup, TaskStatus
from main.models import UserProfile
from drf_writable_nested.serializers import WritableNestedModelSerializer
# from drf_writable_nested.mixins import UniqueFieldsMixin, NestedCreateMixin
# from main.serializers import UserProfileSerializer


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('TaskStatus_No', 'TaskStatus_name')


class TaskGroupSerializer(serializers.ModelSerializer):
    # User = UserProfileSerializer() 
    User = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        # write_only = True
    )

    Task = SerializerMethodField()
    TaskGroup_status = serializers.SlugRelatedField(
        # read_only=False,
        many=False,
        slug_field='TaskStatus_No',
        queryset=TaskStatus.objects.all()
    )

    class Meta:
        model = TaskGroup
        fields = ('User', 'TaskGroupId', 'TaskGroup_status', 'TaskGroup_sortId','TaskGroup_name', 'TaskGroup_created_at', 'TaskGroup_updated_at', 'Task')

    
    def get_Task(self, obj):

        try:
            Task_abstruct_contents = TaskSerializer(Task.objects.all().filter(TaskGroup = TaskGroup.objects.get(TaskGroupId=obj.TaskGroupId)), many=True).data
            return Task_abstruct_contents
        except:
            Task_abstruct_contents = None
            return Task_abstruct_contents




# class TaskGroupSerializer(serializers.ModelSerializer):
#     # User = UserProfileSerializer() 
#     User = serializers.PrimaryKeyRelatedField(
#         queryset=UserProfile.objects.all(),
#         # write_only = True
#     )

#     Task = SerializerMethodField()
#     TaskGroup_status = TaskStatusSerializer(read_only=True)
#     TaskGroup_status_No = serializers.SlugRelatedField(
#         write_only=True,
#         many=False,
#         slug_field='TaskStatus_No',
#         queryset=TaskStatus.objects.all()
#     )

#     class Meta:
#         model = TaskGroup
#         fields = ('User', 'TaskGroupId', 'TaskGroup_status_No', 'TaskGroup_sortId','TaskGroup_name', 'TaskGroup_status', 'TaskGroup_created_at', 'TaskGroup_updated_at', 'Task')

    
#     def get_Task(self, obj):

#         try:
#             Task_abstruct_contents = TaskSerializer(Task.objects.all().filter(TaskGroup = TaskGroup.objects.get(TaskGroupId=obj.TaskGroupId)), many=True).data
#             return Task_abstruct_contents
#         except:
#             Task_abstruct_contents = None
#             return Task_abstruct_contents

#     def update(self,  instance, validated_date):
#         print(" □□□□□□□□□□□")
#         print(validated_date)
#         validated_date['TaskGroup_status'] = validated_date.get('TaskGroup_status_No', None)

#         if validated_date['TaskGroup_status'] is None:
#             raise serializers.ValidationError("TaskGroup_status not found.") 

#         del validated_date['TaskGroup_status_No']

#         return TaskGroup.objects.update(**validated_date)

#     def create(self, validated_date):
#         validated_date['TaskGroup_status'] = validated_date.get('TaskGroup_status_No', None)
#         if validated_date['TaskGroup_status'] is None:
#             raise serializers.ValidationError("TaskGroup_status not found.") 
#         del validated_date['TaskGroup_status_No']

#         return TaskGroup.objects.create(**validated_date)


class TaskSerializer(serializers.ModelSerializer):
    TaskGroup = serializers.PrimaryKeyRelatedField(
        queryset=TaskGroup.objects.all(),
        write_only = True
    )
    List = SerializerMethodField()   

    Task_status = serializers.SlugRelatedField(
        # read_only=False,
        many=False,
        slug_field='TaskStatus_No',
        queryset=TaskStatus.objects.all()
    )
    class Meta:
        model = Task
        # fields = ('TaskGroup', 'TaskId', 'Task_sortId','Task_name', 'Task_status', 'Task_description', 'Task_created_at', 'Task_updated_at')
        fields = ('TaskGroup','TaskId', 'Task_sortId','Task_name', 'Task_status', 'Task_description', 'Task_created_at', 'Task_updated_at', 'List')
        # depth = 1
        

    def get_List(self, obj):

        try:
            List_abstruct_contents = ListSerializer(List.objects.all().filter(Task = Task.objects.get(TaskId=obj.TaskId)), many=True).data
            return List_abstruct_contents
        except:
            List_abstruct_contents = None
            return List_abstruct_contents



class ListSerializer(serializers.ModelSerializer):

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
        # partial=True
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