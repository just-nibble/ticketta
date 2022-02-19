from django.urls import path

from . import views

urlpatterns = [
    path("", views.TicketAPIView.as_view()),
    path("<int:pk>/", views.TickerDetailAPIView.as_view()),
]
