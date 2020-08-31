
from django.urls import path
from shopping_cart import views as shopping_cart_views

app_name = 'shopping_cart'

urlpatterns = [
    path('add_to_cart/<int:item_id>', shopping_cart_views.add_to_cart, name="add_to_cart"),
    path('order_details/', shopping_cart_views.order_details, name='order_details'),
    path('item/delete/<int:item_id>', shopping_cart_views.delete_from_cart, name='delete_item'),
    path('shipping_address/', shopping_cart_views.shipping_address, name='shipping_address'),
    path('checkout', shopping_cart_views.checkout, name='checkout'),
    ]

