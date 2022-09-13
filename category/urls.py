from djngo.urls import path
from category.views import products_list, product_details, category......





urlpatterns = [

    path('product/list/', products_list, name='product-list')
    path('product/search/', products_search, name='product-search')
    path('product/detail/<int:pk>/', product_detail, name='product-detail')
    path('category/<int:pk>/products', category_products, name='category-detail')
    path('profile/', user_profile, name='user-profile')
    path('campaign/', campaign, name='campaign')

]