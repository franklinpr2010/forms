# forms
Trabalhando com forms  

Nesse projeto se trabalhará com mysql, e-mails e forms no django.

Fazer a instalação do django, gunicorn, bootstrap e whitenoise, PyMySql (Drive do mysql), django-std-image( Facilita trabalhar com imagens no projeto ) :  

pip install django whitenoise gunicorn django-bootstrap PyMySql django-std-image  

pip freeze > requirements.txt  

Criando um projeto:  

django-admin startproject django2 .

Criando a aplicação:  

django-admin startapp core

Definindo e configurando as views emn views.py

Enviar emails, criar templates e View para um formulário que salva dados no banco.

Configurando as rotas da aplicação em urls.py  

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [  
    path('admin/', admin.site.urls),  
    #qualquer rota que não tenha envia para outra aplicação, no caso core.urls  
    path('', include('core.core_urls'))  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  



Na urls da aplicação  

from django.urls import path  

from .views import index, contato, produto  

urlpatterns = [  
    path('', index, name='index'),  
    path('contato/', contato, name='contato'),  
    path('produto/', produto, name='produto'),  
]








