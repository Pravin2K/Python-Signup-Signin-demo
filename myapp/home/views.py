from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    data = [
        {'name': 'John', 'age': 29, 'role': 'Softwate Engineer'},
        {'name': 'Devid', 'age': 19, 'role': 'Softwate Developer'},
        {'name': 'Juyal', 'age': 34, 'role': 'Database  Engineer'},
        {'name': 'Henery', 'age': 24, 'role': 'Cloud Engineer'},
        {'name': 'Warner', 'age': 20, 'role': 'React Developer'}
    ]

    text = 'I am a software enginner'

    for users in data:
        print(users)
    return render(request, 'index.html', context={'data' : data, 'text': text,})
