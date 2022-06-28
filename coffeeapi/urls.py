from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)