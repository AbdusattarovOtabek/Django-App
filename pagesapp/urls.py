from .views import *
from django.urls import path,include

urlpatterns = [
    path('', intro, name='intro'),
    path('', include('user.urls')),
    path('product/add/', product_add.as_view(), name='product_add'),
    path('menu/', menu, name='menu'),
    path('product/', menu, name='catalog'),  # 127.0.0.1:8000
    path('product/<int:cat_id>/', tovar, name='catalog'),  # 127.0.0.1:8000/tovar

]
