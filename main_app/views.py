from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name="home.html"

class List(TemplateView):
        template_name='list.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["lists"] = lists
            return context

class List:
    def __init__(self,owner,items):
        self.owner = owner
        self.items = items

lists = [
    List("Ben Baker",['apple','orange','chicken thighs','yogurt']),
    List("Brenna Langille", ['pickles','green cola','sausages','peppers'],
    List("Devin Larsen",['tempeh','grains','ointment','toothpaste']))
]

