from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'store'

urlpatterns = [
    path('', views.ProductView.as_view(), name='ProductView'),
    path('cart', views.OrderItemView.as_view(), name='OrderItemView'),
    path('orders', views.OrderView.as_view(), name='OrderView'),
    path('add', views.AddProduct.as_view(), name='Add'),
    path('addimage', views.AddProductImage.as_view(), name='Addimage'),
    path('addproductwithimage' , views.AddProductWithImage.as_view() , name='Addproductwithimage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)