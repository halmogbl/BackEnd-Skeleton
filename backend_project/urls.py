from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls.static import static
from django.conf import settings



from sekail.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    StoreCreateAPIView,
   
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', obtain_jwt_token, name='login'),
    path('customer/register/', UserCreateAPIView.as_view(), name='customer-register'),
    path('store/register/', StoreCreateAPIView.as_view(), name='store-register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
