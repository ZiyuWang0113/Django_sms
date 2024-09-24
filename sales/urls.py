from django.urls import path

from . import views

urlpatterns = [
    # 不带一级路由表
    path('orders/', views.listorders),

    path('customers/', views.listcustomers),
]
