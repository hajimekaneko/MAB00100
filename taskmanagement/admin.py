from django.contrib import admin

from .models import TaskStatus, List, Task, TaskGroup

admin.site.register(TaskStatus)
# admin.site.register(TaskType)
admin.site.register(TaskGroup)
admin.site.register(Task)
admin.site.register(List)
