from django.db import models

class Book(models.Model):

  title = models.CharField(max_length=100)
  publisher = models.CharField(max_length=100)
  year = models.IntegerField()
  isbn = models.CharField(max_length=13, unique=True)
  backCover = models.TextField()
  cover = models.BooleanField(default=False)

  def __str__(self):
    return self.title
  


class Review(models.Model):
  date = models.DateField(auto_now_add=True)
  text = models.CharField(max_length=250)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

  def __str__(self):
    return f"Avis de {self.book.title} ({self.date})"
