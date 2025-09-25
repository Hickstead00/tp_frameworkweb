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
