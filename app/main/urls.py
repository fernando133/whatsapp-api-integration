from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

admin.site.site_header = "WTM Brazil"
admin.site.index_title = "Administração WTM"
admin.site.site_title = "Painel"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
