from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book_id>/", views.book, name="book"),
    path("new_book", views.new_book, name="new_book"),
    path("delete_book/<int:book_id>", views.delete_book, name="delete_book"),
    path("edit_book/<int:book_id>", views.edit_book, name="edit_book")
]