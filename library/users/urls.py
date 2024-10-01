from django.urls import path

from . import views

urlpatterns = [
    path('', views.users_view, name='all_users'),
    path('<int:user_id>', views.user_by_id, name='user_by_id')
]
