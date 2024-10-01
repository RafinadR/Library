from django.urls import path
from . import views


urlpatterns = [
    path('all_authors/', views.all_authors, name='all_authors'),
    path('author_create/', views.author_create, name='author_create'),
    path('author_delete/<int:author_id>/', views.author_delete, name='author_delete'),
    path('author/<int:author_id>/', views.author_by_id, name='author_by_id'),
    path('author_update/<int:author_id>', views.author_update, name='author_update')
]