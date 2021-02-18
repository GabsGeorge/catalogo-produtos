from django.urls import include, path
from .views import ListaDeProdutosView

urlpatterns =[
    path('lista-de-produtos', ListaDeProdutosView.as_view(), name='lista-de-produtos')
]