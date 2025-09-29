from django.urls import path
from . import views

app_name = "zarinpal"

urlpatterns = [
    path("payment-request/<int:pk>/", views.payment_request, name="payment_request"),
    path("payment-verify/", views.payment_verify, name="payment_verify"),
]

