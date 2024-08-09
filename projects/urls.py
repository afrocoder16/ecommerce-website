from django.urls import path
from . import views
from .import test_api


urlpatterns = [
    path('', views.home, name='home'),  # make your homepage accessible from the root URL
    path('products/', views.product_listing, name='product_listing'),
    path('profile/', views.user_profile, name='user_profile'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('test-api/', views.test_api_response, name='test_api_response'),

]
