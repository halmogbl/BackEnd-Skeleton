from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls.static import static
from django.conf import settings



from sekail.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
   
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/login/', obtain_jwt_token, name='login'),
    path('customer/register/', UserCreateAPIView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
