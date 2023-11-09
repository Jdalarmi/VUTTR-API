from django.urls import path
from api import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('list_all', views.list_all, name='list_all'),
    path('delete_by_id/<int:pk>/', views.delete_by_id, name='delete_by_id'),
    path('search_tag/', views.search_tag, name='search_tag'),
]
