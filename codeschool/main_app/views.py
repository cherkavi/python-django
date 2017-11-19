from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = 'Eva'
    surname = 'Brown'
    context = {'name': name, 'surname': surname}
    return render(request, 'index.html', context)
