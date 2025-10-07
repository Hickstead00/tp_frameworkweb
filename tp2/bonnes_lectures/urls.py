from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book_id>/", views.book, name="book"),
    path("new_book", views.new_book, name="new_book")
]