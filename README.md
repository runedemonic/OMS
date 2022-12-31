# OMS(order management system)

## 요약

* 주문 관리를 위한 웹페이지 제작

## 프로젝트 목표

* 수기로 작성 중인 주문 관리를 웹으로함으로써 관리에 용이하게함
* 최대한 간단하고 직관적인 디자인과 동선

----

## DRF 실습해보기

### DRF

DRF(Django Rest Framework)란Django 안에서 RESTful API 서버를 쉽게 만들게 도와주는 라이브러리다.

Django REST framework를 사용하는 이유는 크게

* 웹 브라우저 API는 범용성이 크다. 개발을 쉽게 만들어준다.
* 시리얼라이즈 기능을 제공해준다. (DB data -> JSON)

### Serializer

Serializer란 말 그대로 직렬화하는 클래스로서, 사용자의 DB안에 사용자 프로필 사진, 이메일, 이름, 성별이 있다고 가정하면 사용자 모델 인스턴스를 JSON 형태 혹은 Dictionary 형태로 직렬화 할
수 있다.

### 실습

1. 모델 생성 

   ```django
   class Order(models.Model):
       company_name = models.CharField(max_length=100)
       product_name = models.CharField(max_length=200)
       product_code = models.CharField(max_length=100, blank=True)
       price = models.IntegerField()
       quantity = models.IntegerField()
       sum = models.IntegerField()
       order_date = models.DateField(auto_now=True)
       due_date = models.DateField(blank=True)
   ```

2. serializer.py 생성

   ```django
   from rest_framework import serializers
   from .models import Order
   
   class OrderSerializer(serializers.ModelSerializer):
       class Meta:
           model = Order
           fields = '__all__'
   
   
   class Order_detailSerializer(serializers.ModelSerializer):
       class Meta:
           model = Order
           fields = '__all__'
   ```

   * OrderSerializer라는 클래스를 생성 후 ModelSerializer를 상속
   * ModelSerializer 클래스를 사용하여 Model에 정의한 필드의 값을 직렬화(serializer)

3. views.py

   ```django
   from django.shortcuts import render, get_object_or_404
   from rest_framework import viewsets
   from rest_framework.response import Response
   from .serializers import *
   from .models import *
   from django.http import HttpResponse
   from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
   # Create your views here.
   
   class OrderViewSet(viewsets.ModelViewSet):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer
   
   
   class Order_detail(RetrieveAPIView):
       lookup_field = 'id'
       queryset = Order.objects.all()
       serializer_class = Order_detailSerializer
   
   
   class Order_Update(UpdateAPIView):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer
   
   
   class Order_delete(DestroyAPIView):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer
   
   class Order_create(CreateAPIView):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer
   ```

   

4. urls.py

   1. OMS/urls.py

      ```django
      urlpatterns = [
          path('admin/', admin.site.urls),
          path("", include("order.urls")),
      ]
      ```

      

   2. order/urls.py

      ```django
      from django.urls import path, re_path, include
      from . import views
      from rest_framework import routers
      from .views import *
      
      router = routers.DefaultRouter()
      router.register('order', OrderViewSet)
      
      app_name = 'order'
      
      urlpatterns = [
          # path('',include(router.urls))
          path('', OrderViewSet.as_view({'get': 'list'}), name='order_list'),
          path('detail/<int:id>/', Order_detail.as_view(), name='order_detail'),
          path('update/<int:id>/', Order_Update.as_view(), name='order_update'),
          path('delete/<int:id>/', Order_delete.as_view(), name='order_delete'),
          path('create', Order_create.as_view(), name='order_create'),
      ]
      
      ```

기본적인 CRUD를 구현

* 삭제가 제대로 안됨
