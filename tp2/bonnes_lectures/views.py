from django.shortcuts import render
from django.http import HttpResponse

def about(request):
  return HttpResponse("Bienvenue dans l'application 'Bonnes lectures'")

def welcome(request):
  return render(request, 'bonnes_lectures/welcome.html')
