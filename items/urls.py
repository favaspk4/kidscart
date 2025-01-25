from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('index.html',views.home_view,name='home'),
    path('contact.html',views.contact_view,name='contact'),
    path('blog.html',views.blog_view,name='blog'),
    path('blog-details.html',views.blogdetails_view,name='blog-details'),
    path('product-details.html',views.productdetails_view,name='product-details'),
    path('shop-cart.html',views.shopcart_view,name='shop-cart'),
    path('checkout.html',views.checkout_view,name='checkout'),
    path('shop.html',views.shop_view,name='shop'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
]
