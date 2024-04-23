from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class LaptopView(TemplateView):
    template_name = 'laptop.html'
    
class ProductView(TemplateView):
    template_name = 'product.html'

class ComputerView(TemplateView):
    template_name = 'computer.html'


# Create your views here.
