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
    reviews = book.reviews.all()
  except Book.DoesNotExist:
    raise Http404("Le livre n'existe pas")
  return render(request, "bonnes_lectures/book.html", {"book":book, "reviews":reviews})

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

def edit_book(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  if request.method == "POST":
    form = BookForm(request.POST, instance=book)
    id = check_save(form)
    return redirect("book", book_id=id)
  else:
    form = BookForm(instance=book)
  return render(request, "bonnes_lectures/book_form.html",{"form": form, "button_label": "Modifier"})


def check_save(form):
  if form.is_valid():
    book = form.save(commit=False)
    book.save()
  return book.id

def welcome(request):
  return render(request, "bonnes_lectures/welcome.html")

def add_review(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.book = book
      review.save()
      return redirect("book", book_id=book.id)
  else:
    form = ReviewForm()
  return render(request, 'bonnes_lectures/review_form.html', {'form':form, 'book':book})


def edit_review(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  if request.method == 'POST':
    form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
      form.save()
      return redirect("book", book_id=review.book.id)
  else:
    form = ReviewForm(instance=review)
  return render(request, 'bonnes_lectures/review_form.html', {'form':form, 'book':review.book})

def delete_review(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  book_id = review.book.id
  if request.method == 'POST':
    review.delete()
    return redirect('book', book_id=review.book.id)
  return render(request, 'bonnes_lectures/review_confirm_delete.html', {'review':review, 'book':review.book})

def add_author(request):
  if request.method == 'POST':
    form = AuthorForm(request.POST)
    if form.is_valid():
      author = form.save(commit=False)
      author.save()
    return redirect('author_list')
  else:
    form = AuthorForm()
  return render(request, "bonnes_lectures/author_form.html", {"form":form})

def author_list(request):
  authors = Author.objects.all()
  return render(request, "bonnes_lectures/author_list.html", {"all_authors": authors})


