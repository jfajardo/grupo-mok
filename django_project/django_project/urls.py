from django.contrib import admin
from django.urls import path, include

from helpers.doc_schema_view import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.api.urls', namespace='api')),
    path('auth/', include('djoser.urls')),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls.authtoken')),
]