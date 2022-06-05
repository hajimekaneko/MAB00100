from django.urls import path, include
from rest_framework import routers


from . import views
router = routers.SimpleRouter()
router.register('users', views.UserProfileViewSet)

app_name = 'main_apiv1'
urlpatterns = [
    path('login/', views.UserProfileLoginAPIView.as_view()),
    path('signup/', views.UserProfileSignupAPIView.as_view()),
    path('logout/', views.UserProfileLogoutAPIView.as_view()),
    path('google/', views.GoogleLoginView.as_view(), name='google'),
    path('', include(router.urls)),
]

