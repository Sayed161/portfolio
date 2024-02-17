from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from blog.models import Blog
from contact.models import Contact
from contact.forms import ContactForm
from projects.models import Projects,Service
# Create your views here.
class Index(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["Blog"] = Blog.objects.all()
        context["project"] = Projects.objects.all()
        context["service"] = Service.objects.all()
        return context
    
    
    

    

    