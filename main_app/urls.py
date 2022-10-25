from django.urls import path
from . import views
from .views import index


# this like app.use() in express
urlpatterns = [
    path("", index, name="index"),
    path('lists/',views.List.as_view(), name='list')
]