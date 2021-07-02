from django.urls import path
from .views import Home, success, TestPayment, PaypalPaymnet, payment_complete
urlpatterns = [
   
    path('',Home.as_view(), name="home"),
    path('success/',success, name="success"),
    path('test/', TestPayment.as_view(), name="test"),
    path("paypal/", PaypalPaymnet.as_view(), name = "paypal"),
    path("complete", payment_complete, name = "complete"),
]
