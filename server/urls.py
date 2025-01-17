from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from server import settings

from authentication.views import *
from rest_api.views import *


router = routers.DefaultRouter()
# router.register(r'manager/signin', ManagerSigninAPI, basename='manager_signin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('rest_api.urls')),
    # path('api/v1/', include(router.urls)),

]

websocket_urlpatterns = [
    path('web_socket/group_chats/<uuid:group_id>/', GroupChatConsumer.as_asgi()),
    path('web_socket/private_chat/<uuid:sender_id>/<uuid:recepient_id>/', PrivateChatConsumer.as_asgi()),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)