from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('books', book, name="books"),
    path('detail/<int:id>/', book_detail, name="detail"),
    path('signup', registration, name="signup"),
    path('login', user_login, name="login"),
    path('profile', user_profile, name="profile"),
    path('logout', user_logout, name="logout"),
    path('update_profile', update_profile, name="update_profile"),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart_delete/<int:cart_item_id>/', cart_delete, name='cart_delete'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_URL)
