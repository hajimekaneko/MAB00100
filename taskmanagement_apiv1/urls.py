from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('task_groups', views.TaskGroupViewSet)
router.register('tasks', views.TaskViewSet)
router.register('lists', views.ListViewSet)


app_name = 'taskmanagement_apiv1'
urlpatterns = [
    path('fetch_lists/', views.FetchListAPIView.as_view()),
    path('', include(router.urls)),
]

