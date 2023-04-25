from django.contrib import admin
from django.urls import path,include
from .views import UserRegisterView,AuthorRegisterView,UserLoginView,AuthorDashBoardView,UserDashboardView,Cart,Checkout,Contactus,Newarrivals,Bestsellers
from django.contrib.auth.views import LogoutView
from .import views
urlpatterns = [
 
 path('userregister/',UserRegisterView.as_view(),name='userregister'),
 path('authorregister/',AuthorRegisterView.as_view(),name='authorregister'),
 path('login/',UserLoginView.as_view(),name='login'),
 path('logout/',LogoutView.as_view(),name='logout'),
 path('user/dashboard/',UserDashboardView.as_view(),name='user_dashboard'),
 path('author/dashboard/',AuthorDashBoardView.as_view(),name='author_dashboard'),
 path('aboutus/',views.aboutus,name='aboutus'),
 path('newarrivals/',Newarrivals.as_view(),name='new_arrivals'),
 path('bestsellers/',Bestsellers.as_view(),name='best_sellers'),
#  path('tv/',views.tv,name='tv'),
#  path('movies/',views.movies,name='movies'),
#  path('celebs/',views.celebs,name='celebs'),
#  path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
#  path('cart/',Cart.as_view(),name='cart'),
 path('checkout/',Checkout.as_view(),name='checkout'),
 path('contactus/',Contactus.as_view(),name='contact_us'),
#cart
 path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
 path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
 path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
 path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
 path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
 path('cart/',views.cart_detail,name='cart'),
]
