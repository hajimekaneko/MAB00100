from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('tasks', views.TaskViewSet)
router.register('lists', views.ListViewSet)

app_name = 'taskmanagement_apiv1'
urlpatterns = [
    path('', include(router.urls)),
]

