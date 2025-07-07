# joinventureai/urls.py
from django.contrib import admin
from django.urls import path
from authentication.views import UserRegistrationView, UserLoginView, UserProfileView
from payments.views import CreateCheckoutSessionView, PaymentSuccessView, PaymentCancelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/signup/', UserRegistrationView.as_view(), name='signup'),
    path('api/authentication/login/', UserLoginView.as_view(), name='login'),
    path('api/user_profile/get_user_profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/payment/create_checkout/', CreateCheckoutSessionView.as_view(), name='create-checkout'),
    path('api/payment/success/', PaymentSuccessView.as_view(), name='payment-success'),
    path('api/payment/cancel/', PaymentCancelView.as_view(), name='payment-cancel'),
]