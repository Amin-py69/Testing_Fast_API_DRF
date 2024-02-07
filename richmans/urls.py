from django.conf.urls.static import static
from django.urls import path

from Testing_Fast_API_DRF import settings
from richmans.views import RichManViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)

router = DefaultRouter()
router.register(r'richman', RichManViewSet, basename='richman')
urlpatterns += router.urls
