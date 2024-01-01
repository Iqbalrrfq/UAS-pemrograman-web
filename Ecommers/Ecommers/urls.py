from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('shop_detail/', include('shop_detail.urls')),
    path('contact/', include('contact.urls')),
    path('', views.index),
]
