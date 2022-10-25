from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django_nextjs.render import render_nextjs_page_sync
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name="home.html"

class List(TemplateView):
        template_name='list.html'
        model = list
   


def index(request):
    return render_nextjs_page_sync(request)