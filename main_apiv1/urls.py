from django.urls import path, include
from rest_framework import routers


from . import views
router = routers.SimpleRouter()
router.register('users', views.UserProfileViewSet)

app_name = 'main_apiv1'
urlpatterns = [
    path('login/', views.UserProfileLoginAPIView.as_view()),
    path('logout/', views.UserProfileLogoutAPIView.as_view()),
    path('', include(router.urls)),
]

