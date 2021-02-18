from django.shortcuts import render
from django.views.generic import TemplateView

class ListaDeProdutosView(TemplateView):
    template_name = "catalogo/catalogo.html"

# Create your views here.

