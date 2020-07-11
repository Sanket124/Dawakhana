from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminpage,name='adminhome'),
    path('shopDetails/<shop_id>', views.shopDetails, name='shopDetails'),
    path('shopDetails/final/', views.final, name='final'),
]