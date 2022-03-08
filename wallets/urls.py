from django.urls import path
from .import views

urlpatterns = [
    path('', views.WithdrawalAPIView.as_view())
]
