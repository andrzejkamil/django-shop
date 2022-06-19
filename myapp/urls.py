from django.urls import path
from . import views

app_name= "myapp"
urlpatterns = [
    path('', views.index, name = "index"),
    path('products/', views.products, name = "products"),
    path('products/<int:id>/', views.product_detail, name = "product_detail"),
    path('products/add/', views.add_product, name = "add_product"),
    path('products/update/<int:id>/', views.update_product, name = "update_product"),
]
