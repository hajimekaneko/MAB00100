from django.urls import path

from . import views

# router.register('auth/login', views.AuthViewSet)

app_name = 'main_apiv1'
urlpatterns = [
    path('login/', views.AuthLoginAPIView.as_view()),
    path('logout/', views.AuthLogoutAPIView.as_view()),
]

