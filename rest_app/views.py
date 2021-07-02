from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return  context

def success(request):
    if request.method == "POST":
        charge = stripe.Charge.create(
            amount = 500,
            currency = "inr",
            description = "Test stripe payment with django",
            source = request.POST["stripeToken"]
        )
        data = stripe.Charge.retrieve(charge.id)
        charge_list = stripe.Charge.list(limit=3)
        
        return render (request, "success.html", {"charge":data.id, "charge_list":charge_list})
        

class TestPayment(APIView):
  def post(self, request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000, 
        currency='pln', 
        payment_method_types=['card'],
        receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)
    
    
class PaypalPaymnet(TemplateView):
  template_name = "index.html"
  

def payment_complete(request):
  body = json.loads(request.body)
  print("body: ", body)
  return JsonResponse(body, safe=False)
