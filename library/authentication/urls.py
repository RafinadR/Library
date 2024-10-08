from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login')
]
