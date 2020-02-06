from django.urls import path

#nesse pacote views importa o index, contato e produto
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    #envia para a view contato
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]



