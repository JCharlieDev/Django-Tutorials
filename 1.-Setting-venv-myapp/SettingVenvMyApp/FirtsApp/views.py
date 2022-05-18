from itertools import count
from django import views
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'Mexican'
    }

    name = "Charlie"
    return render(request, 'index.html', context)

def counter(request):

    text = request.POST["text"]
    numberOfWords = len(text.split())

    return render(request, 'counter.html', {'amount': numberOfWords})