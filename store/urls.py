from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('liked-products/', views.liked_products, name='liked_products'),
    path('ordered-products/', views.ordered_products, name='ordered_products'),
    path('market/', views.market, name='market'),
    path('profil/', views.profil, name='profil'),
    path('profil2/', views.profil2, name='profil2'),
    path('competition/', views.competition, name='competition'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('admin-pagewithdraw/', views.admin_pagewithdraw, name='admin_pagewithdraw'),
    path('requests/', views.requests_view, name='requests'),
    path('stats/', views.stats, name='stats'),
    path('changelog/', views.changelog, name='changelog'),
    path('widgets/', views.widgets, name='widgets'),
]