from django.urls import path
from . import views

urlpatterns = [
    path("all_books/", views.all_books, name="all_books"),
    path("add/", views.add, name="add"),
    path("view_book/<int:book_id>/", views.view_book, name="view_book"),
    path("book/<int:book_id>/delete/", views.delete_book, name="delete_book"),
    path("book/user_books/<int:user_id>/", views.user_books, name="user_books")
    

]