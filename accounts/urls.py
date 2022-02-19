from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
    path('login/', views.LoginView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path('registration/account-confirm-email/')
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('register/', include('dj_rest_auth.registration.urls'))
    # path('register/', views.CustomRegisterView.as_view()),
]
