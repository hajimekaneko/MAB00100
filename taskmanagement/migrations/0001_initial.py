# Generated by Django 4.0.2 on 2022-05-03 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('TaskStatusId', models.AutoField(primary_key=True, serialize=False)),
                ('TaskStatus_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='名前')),
            ],
            options={
                'db_table': 'TaskStatus',
            },
        ),
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('TaskGroupId', models.AutoField(primary_key=True, serialize=False)),
                ('TaskGroup_sortId', models.IntegerField(blank=True, null=True, verbose_name='ソートキー')),
                ('TaskGroup_name', models.CharField(blank=True, max_length=20, verbose_name='名前')),
                ('TaskGroup_created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('TaskGroup_updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('TaskGroup_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmanagement.taskstatus')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TaskGroup',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('TaskId', models.AutoField(primary_key=True, serialize=False)),
                ('Task_sortId', models.IntegerField(blank=True, null=True, verbose_name='ソートキー')),
                ('Task_name', models.CharField(blank=True, max_length=20, verbose_name='名前')),
                ('Task_description', models.TextField(blank=True, null=True, verbose_name='タスクの内容')),
                ('Task_created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('Task_updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('TaskGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanagement.taskgroup')),
                ('Task_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmanagement.taskstatus')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('ListId', models.AutoField(primary_key=True, serialize=False)),
                ('List_sortId', models.IntegerField(blank=True, null=True, verbose_name='ソートキー')),
                ('List_name', models.CharField(blank=True, max_length=20, verbose_name='名前')),
                ('List_memo', models.CharField(blank=True, max_length=20, null=True, verbose_name='メモ')),
                ('List_created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('List_updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('List_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmanagement.taskstatus')),
                ('Task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanagement.task')),
            ],
            options={
                'db_table': 'list',
            },
        ),
    ]
