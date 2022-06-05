from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/taskmanagement/', include('taskmanagement_apiv1.urls')),
    path('api/v1/main/', include('main_apiv1.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    # path('api/v1/social/login/', include('main_apiv1.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
