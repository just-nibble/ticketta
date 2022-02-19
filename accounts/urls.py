from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
    path('login/', views.LoginView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
