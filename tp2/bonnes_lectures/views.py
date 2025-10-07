from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from bonnes_lectures.models import *
from bonnes_lectures.forms import *


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

def new_book(request):
  if request.method == "POST":
    form = BookForm(request.POST)
    if form.is_valid():
      book = form.save(commit=False)
      book.save()

    return HttpResponseRedirect(f"/bl/book/{book.id}")
  else:
    form = BookForm()
  
  return render(request, "bonnes_lectures/book_form.html", {"form": form})

def delete_book(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  if request.method == "POST":
    book.delete()
    return redirect("index")
  
  return render(request, "bonnes_lectures/delete_book.html", {"book": book})