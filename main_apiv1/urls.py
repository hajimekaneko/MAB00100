from django.urls import path

from . import views

app_name = 'main_apiv1'
urlpatterns = [
    path('login/', views.UserProfileLoginAPIView.as_view()),
    path('logout/', views.UserProfileLogoutAPIView.as_view()),
]

