from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
	path('', views.KeyCode, name='home'),
	path('print/', views.PrintOptions, name='print'),
	path('KeyCode/', views.send_email_view, name='key-code'),
	path('stock/', views.StockListView.as_view(), name='stock'),
	path('key/new/', views.create_post, name='new-key'),
	path('key/<int:pk>/', views.key_detail, name='key-detail'),
	path('key/<int:pk>/delete/', views.key_delete, name='key-delete'),
	path('key/<int:pk>/update/', views.key_update, name='key-update'),
	path('key/search/', views.search, name='search'),
]