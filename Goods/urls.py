from django.urls import path, include
from django.contrib.auth import views as auth_views
from Goods import views
from . import views


urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('product/create/', views.createProduct, name='createProduct'),
    path('product/edit/<int:id>/', views.product_update, name='product_update'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
]