from . views import DetailView
from django.urls import path

urlpatterns = [
    path('projects/<int:pk>', DetailView.as_view(), name='detail'),

]