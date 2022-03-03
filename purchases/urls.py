from django.urls import path

from . import views

urlpatterns = [
    path('', views.PurchaseAPIView.as_view()),
    path('<slug:slug>/', views.PurchaseDetailAPIView.as_view()),
    path('<slug:slug>/use/', views.PurchaseUseAPIView.as_view())

]
