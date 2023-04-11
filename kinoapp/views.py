from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'kinoapp/index.html')

def blog(request):
    return render(request, 'kinoapp/blog.html')

def categories(request):
    return render(request, 'kinoapp/categories.html')

def anime_details(request):
    return render(request, 'kinoapp/anime_details.html')

def anime_watching(request):
    return render(request, 'kinoapp/anime_watching.html')

def blog_details(request):
    return render(request, 'kinoapp/blog_details.html')

def login(request):
    return render(request, 'kinoapp/login.html')

def signup(request):
    return render(request, 'kinoapp/signup.html')