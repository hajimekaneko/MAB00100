from django.db import models
from django.db.models.fields.related import ForeignKey

class List(models.Model):
    """LISTモデル"""

    class Meta:
        db_table = 'list'

    listId = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='name', max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    """Taskモデル"""

    class Meta:
        db_table = 'task'

    taskId = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='name', max_length=20, null=True, blank=True)
    description = models.TextField(verbose_name='items', null=True, blank=True)
    list = ForeignKey(List, related_name='tasks', verbose_name="リスト", on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    def __str__(self):
        return self.name