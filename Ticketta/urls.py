"""Ticketta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

# rest framework imports
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# project imports
from Ticketta import settings

API_TITLE = 'Ticketter Docs'
API_DESCRIPTION = 'A Web API for ticketting'

schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
        description=API_DESCRIPTION,
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('docs/', include_docs_urls(
        title=API_TITLE,
        description=API_DESCRIPTION)
    ),
    path('events/', include('events.urls')),
    path('purchases/', include('purchases.urls')),
    path('reddocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name="redoc-ui"),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('tickets/', include('tickets.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
