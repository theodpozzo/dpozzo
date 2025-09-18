from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Language

def example_view(request):
    # Example
    language1 = {
        "name": "English",
        "letter": "E",
        "colour": "#FF5733",
    }
    language2 = {
        "name": "French",
        "letter": "F",
        "colour": "#33C1FF",
    }

    book1 = {
        "title": "Test Book 1",
        "description": "This is a test book description.",
        "language": language1
    }
    book2 = {
        "title": "Test Book 2",
        "description": "second description",
        "language": language1
    }
    book3 = {
        "title": "Test Book 3",
        "description": "third description",
        "language": language2
    }
    
    books = [book1, book3, book2]
    return books



def home(request):
    books = example_view(request)
    books = None

    context = {
        "name": "Theo Dal Pozzo",
        "title": "Welcome to my portfolio website!",
        "linkedin": "https://www.linkedin.com/in/theo-dal-pozzo/",
        "github": "https://www.github.com/theodpozzo",
        "email": "theo@dpozzo.com",
        "books": books,
        }
    return render(request, "core/home.html", context)
