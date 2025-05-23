from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('product/', views.product, name='product'),
    path('admin-page/', views.admin_page, name='admin_page'),
    # Kerakli boshqa yo'nalishlarni qo'shing.
]
