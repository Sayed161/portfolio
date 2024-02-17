from django.shortcuts import render
from . models import Projects
from django.views.generic import DetailView
# Create your views here.

class DetailView(DetailView):
    model = Projects
    template_name = "projects.html"