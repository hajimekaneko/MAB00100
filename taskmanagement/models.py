from django.db import models
from django.db.models.fields.related import ForeignKey

from main.models import UserProfile

class TaskStatus(models.Model):
    """Statusモデル"""

    class Meta:
        db_table = 'TaskStatus'

    TaskStatusId = models.AutoField(primary_key=True)
    TaskStatus_name = models.CharField(verbose_name='名前', max_length=20, null=False, blank=False)
    TaskStatus_No = models.IntegerField(verbose_name='ステータスId', null=False, blank=False)

    def __str__(self):
        return self.TaskStatus_name

class TaskGroup(models.Model):
    """Groupモデル"""

    class Meta:
        db_table = 'TaskGroup'

    User = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    TaskGroupId = models.AutoField(primary_key=True)
    TaskGroup_sortId = models.IntegerField(verbose_name='ソートキー', null=True, blank=True)
    # TaskGroup_TaskType = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=False)
    TaskGroup_name = models.CharField(verbose_name='名前', max_length=20, null=False, blank=True)
    TaskGroup_status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, default=1, null=False)
    TaskGroup_created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    TaskGroup_updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.TaskGroup_name


class Task(models.Model):
    """Taskモデル"""

    class Meta:
        db_table = 'task'

    TaskGroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, null=False)
    # Task_TaskType = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=False)
    TaskId = models.AutoField(primary_key=True)
    Task_sortId = models.IntegerField(verbose_name='ソートキー', null=True, blank=True)
    Task_name = models.CharField(verbose_name='名前', max_length=20, null=False, blank=True)
    Task_status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, default=1, null=False)
    Task_description = models.TextField(verbose_name='タスクの内容', null=True, blank=True)
    Task_created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    Task_updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.Task_name


class List(models.Model):
    """LISTモデル"""

    class Meta:
        db_table = 'list'
    Task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    # List_TaskType = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=False)
    ListId = models.AutoField(primary_key=True)
    List_sortId = models.IntegerField(verbose_name='ソートキー', null=True, blank=True)
    List_name = models.CharField(verbose_name='名前', max_length=20, null=False, blank=True)
    List_status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, default=1, null=False)
    List_memo = models.CharField(verbose_name='メモ', max_length=20, null=True, blank=True)
    List_created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    List_updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.List_name