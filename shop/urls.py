from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('shop/products/',views.product_list,name="products"),
    path('shop/product-detail/<int:id>',views.product_details,name="product_details")
]