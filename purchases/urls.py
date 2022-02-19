from django.urls import path

from . import views

urlpatterns = [
    path('', views.PurchaseAPIView.as_view())
]
