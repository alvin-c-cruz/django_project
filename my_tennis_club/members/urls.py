from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
    path('member/new/', views.member_create, name='member_create'),
    path('member/<int:pk>/edit/', views.member_update, name='member_update'),
    path('member/<int:pk>/delete/', views.member_delete, name='member_delete'),
]
