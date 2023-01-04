from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
from .views import *


app_name = 'order'

urlpatterns = [
    # path('',include(router.urls))
    path('', OrderList.as_view(), name='order_list'),
    path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)