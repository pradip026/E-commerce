from.import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('shop',views.productshow,name='shop'),
    path('features',views.shoppingcart),
    path('blog',views.blog),
    path('blog-detail',views.blogdetail),
    path('product-detail',views.productdetail,name='product-details'),
    path('about',views.about),
    path('contact/',views.contactshop),
    path('message',views.messageshop),
    path('loginform',views.loginform),
    path('signupform',views.signupform),
    path('logout',views.logoutform),
    path('placeorder',views.placeorder),
    path('reviewitem',views.reviewitem),
    path('search_my_item',views.search_my_item),
    path('track_order',views.track_order),

]