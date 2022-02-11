from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('tasks', views.TaskViewSet)
router.register('lists', views.ListViewSet)
# router.register('auth/login', views.AuthViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('auth/login/', views.AuthLoginAPIView.as_view()),
    path('auth/logout/', views.AuthLogoutAPIView.as_view()),
    path('', include(router.urls)),
]

