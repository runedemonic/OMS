from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('order', OrderViewSet)

app_name = 'order'

urlpatterns = [
    # path('',include(router.urls))
    path('', OrderViewSet.as_view(), name='order_list'),
    path('detail/<int:id>/', Order_detail.as_view(), name='order_detail'),
    path('update/<int:id>/', Order_Update.as_view(), name='order_update'),
    path('delete/<int:id>/', Order_delete.as_view(), name='order_delete'),
    path('create', Order_create.as_view(), name='order_create'),
]
