from django.urls import path
from .views import homeview, ContactView, AboutView, LaptopView, ProductView, ComputerView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('laptop/', LaptopView.as_view(), name="laptop_page"),
    path('product/', ProductView.as_view(), name="product_page"),
    path('computer/', ComputerView.as_view(), name="computer_page")
]