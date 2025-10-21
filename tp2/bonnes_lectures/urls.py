from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.welcome, name="welcome"),
    path("book/<int:book_id>/", views.book, name="book"),
    path("new_book", views.new_book, name="new_book"),
    path("delete_book/<int:book_id>", views.delete_book, name="delete_book"),
    path("edit_book/<int:book_id>", views.edit_book, name="edit_book"),
    path("book/<int:book_id>/reviews/add/", views.add_review, name='add_review'),
    path("reviews/<int:review_id>/edit/", views.edit_review, name='edit_review'),
    path("reviews/<int:review_id>/delete", views.delete_review, name='delete_review'),
]