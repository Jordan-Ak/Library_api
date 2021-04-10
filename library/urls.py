"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import ConfirmEmailView, EmailVerificationSentView
from users.views import CustomPasswordTokenVerificationView
from books.api import router



urlpatterns = [
    path('admin/', admin.site.urls),
   
    #This is to verify email after registration
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view()), 

    #Third party package django password reset to reset passwords with email
    path('dj-rest-auth/password/reset/', include('django_rest_passwordreset.urls',)), 
    path('password/reset/verify-token/', CustomPasswordTokenVerificationView.as_view()), 
    #Verify password reset tokens   
    
    #Third party package rest-auths for user registration and authentication with email account activation
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/registration/account-confirm-email/', EmailVerificationSentView.as_view(),
        name='account_email_verification_sent'),

    #To enable quick login and logout restframework
    path('api-auth', include('rest_framework.urls')),

    #Books app related urls
    path('api/v1/', include(router.urls)),
    
    
]
