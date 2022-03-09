from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.PurchaseAPIView.as_view()),
    path('<slug:slug>/detail', views.PurchaseDetailAPIView.as_view()),
    path('<slug:slug>/use/', views.PurchaseUseAPIView.as_view()),
    path("trans/", views.TransacAPIView.as_view()),
    path("djangoflutterwave/", include("djangoflutterwave.urls",
         namespace="djangoflutterwave")),

]
