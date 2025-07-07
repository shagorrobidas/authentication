# payments/views.py
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.urls import reverse
from authentication.models import UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        domain = "http://localhost:8000"  # Change to your domain in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': settings.STRIPE_PRICE_ID,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=domain + reverse('payment-success'),
            cancel_url=domain + reverse('payment-cancel'),
            customer_email=request.user.email,
        )
        return Response({'checkout_url': checkout_session.url})


class PaymentSuccessView(APIView):
    def get(self, request, *args, **kwargs):
        # In a real app, you should verify the session ID and payment status
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.is_subscribed = True
        user_profile.save()
        return Response({'status': 'subscription activated'})


class PaymentCancelView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'status': 'payment cancelled'})