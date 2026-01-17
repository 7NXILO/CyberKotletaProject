from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Тест фреймворка Джанго</h1>")

def about(request):
    return HttpResponse("<button>КнопкаКнопка</button>")

def help(request):
    return HttpResponse("<h1>Эта страница помощи, помоги себе сам</h1>" \
    "<button>Вызов МЧС</button>")