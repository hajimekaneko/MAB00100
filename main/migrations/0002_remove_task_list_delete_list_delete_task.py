# Generated by Django 4.0.2 on 2022-03-26 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='list',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]