from itertools import count
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.isTrue = True
    feature1.details = 'Our service is really quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.isTrue = True
    feature2.details = 'Our service is really Reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to Use'
    feature3.isTrue = False
    feature3.details = 'Our service is really is Easy to Use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.isTrue = True
    feature4.details = 'Our service is really Affordable'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Tarustwhorthy'
    feature5.isTrue = True
    feature5.details = 'Our service is filled with trust'

    features = [feature1, feature2, feature3, feature4, feature5]

    return render(request, 'index.html', {'features': features })

def counter(request):

    text = request.POST["text"]
    numberOfWords = len(text.split())

    return render(request, 'counter.html', {'amount': numberOfWords})