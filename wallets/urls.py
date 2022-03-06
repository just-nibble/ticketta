from django.urls import path
from .import views

urlpatterns = [
    path('', views.WalletList.as_view(), name="wallet_list"),
    path(
        'detail/<int:pk>/',
        views.WalletDetail.as_view(),
        name="wallet_detail"
    ),
    path('transfer', views.Transfer.as_view(), name="transfer"),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
