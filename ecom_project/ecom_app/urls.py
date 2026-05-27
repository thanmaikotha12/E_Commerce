from django.urls import path
from .views import add_product, view_all_products, delete_by_id,add_to_cart,update_product,remove_from_cart,view_cart

#http://127.0.0.1:8000/product/add_product
#http://127.0.0.1:8000/product/view_all_products
urlpatterns=[
    path("add_product",add_product),
    path("view_all_products",view_all_products),
    path("delete_by_id/<int:product_id>/", delete_by_id),
    path("add_to_cart/<int:product_id>/", add_to_cart),
    path("update_product/<int:product_id>/", update_product),
    path("remove_from_cart/<int:cart_id>/", remove_from_cart),
    path("view_cart/", view_cart),
]
