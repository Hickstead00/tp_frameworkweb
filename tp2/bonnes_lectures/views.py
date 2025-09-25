from django.shortcuts import render
from django.http import HttpResponse, Http404
from bonnes_lectures.models import *


def index(request):
  books = Book.objects.order_by("-year")
  context = {"all_books": books}
  return render(request, "bonnes_lectures/books.html", context)

def book(request, book_id):
  try:
    book = Book.objects.get(pk=book_id)
  except Book.DoesNotExist:
    raise Http404("Le livre n'existe pas")
  return render(request, "bonnes_lectures/book.html", {"book":book})