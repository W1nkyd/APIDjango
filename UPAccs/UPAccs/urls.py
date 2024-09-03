"""
URL configuration for UPAccs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Jewelry/', JewelryAPIView.as_view(), name='jewelry-list'),
    path('api/Jewelry/<int:pk>/', JewelryAPIView.as_view(), name='jewelry-detail'),
    path('api/Client/', ClientAPIView.as_view(), name='client-list'),
    path('api/Client/<int:pk>/', ClientAPIView.as_view(), name='client-detail'),
    path('api/Material/', MaterialAPIView.as_view(), name='material-list'),
    path('api/Material/<int:pk>/', MaterialAPIView.as_view(), name='material-detail'),
    path('api/OrderStatus/', OrderStatusAPIView.as_view(), name='orderstatus-list'),
    path('api/OrderStatus/<int:pk>/', OrderStatusAPIView.as_view(), name='orderstatus-detail'),
    path('api/Order/', OrderAPIView.as_view(), name='order-list'),
    path('api/Order/<int:pk>/', OrderAPIView.as_view(), name='order-detail'),
    path('api/Review/', ReviewAPIView.as_view(), name='review-list'),
    path('api/Review/<int:pk>/', ReviewAPIView.as_view(), name='review-detail'),
    path('api/JewelryType/', JewelryTypeAPIView.as_view(), name='jewelrytype-list'),
    path('api/JewelryType/<int:pk>/', JewelryTypeAPIView.as_view(), name='jewelrytype-detail'),
    path('api/OrderComposition/', OrderCompositionAPIView.as_view(), name='ordercomposition-list'),
    path('api/OrderComposition/<int:pk>/', OrderCompositionAPIView.as_view(), name='ordercomposition-detail'),
    path('api/Specialization/', SpecializationAPIView.as_view(), name='specialization-list'),
    path('api/Specialization/<int:pk>/', SpecializationAPIView.as_view(), name='specialization-detail'),
    path('api/Master/', MasterAPIView.as_view(), name='master-list'),
    path('api/Master/<int:pk>/', MasterAPIView.as_view(), name='master-detail'),
    path('api/Production/', ProductionAPIView.as_view(), name='production-list'),
    path('api/Production/<int:pk>/', ProductionAPIView.as_view(), name='production-detail'),
    path('api/MaterialUsage/', MaterialUsageAPIView.as_view(), name='materialusage-list'),
    path('api/MaterialUsage/<int:pk>/', MaterialUsageAPIView.as_view(), name='materialusage-detail'),
    path('api/User/', UserAPIView.as_view(), name='user-list'),
    path('api/User/<int:pk>/', UserAPIView.as_view(), name='user-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('accounts/', include('allauth.urls')),
]
