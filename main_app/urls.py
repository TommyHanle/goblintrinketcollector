from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trinkets/', views.trinkets_index, name='index'),
    path('trinkets/<int:trinket_id>/', views.trinkets_detail, name='detail'),
    path('trinkets/create/', views.TrinketCreate.as_view(), name='trinkets_create'),
    path('trinkets/<int:pk>/update/', views.TrinketUpdate.as_view(), name='trinkets_update'),
    path('trinkets/<int:pk>/delete/', views.TrinketDelete.as_view(), name='trinkets_delete'),
    path('trinkets/<int:trinket_id>/add_uses/', views.add_uses, name='add_uses'),
]

