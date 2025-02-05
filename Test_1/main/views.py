from django.shortcuts import render

def index(requst):
    #Словарь для объектов
    data = {
       'title': 'Главная страница',
       'values': ['Some', 'Hello', 'About'],
       'obj': {
            'car': 'BMW',
       }
    }
    return render(requst, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')