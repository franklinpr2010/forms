from django.db import models
from stdimage.models import StdImageField

#SIGNALS
#Signals - antes ou depois de inserir algo no banco faz algo com esses dados
#Slug - Qualquer coisa que queira separado por traços na url's, titulo da página
from django.db.models import signals
from django.template.defaultfilters import slugify


#Classe base para não repetir campos
class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    #duas casas decimais após a virgula
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    #variations, cria uma variação com a variavel que foi explicitada
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

#Antes de salvar executa a função quando produto enviar um sinal
signals.pre_save.connect(produto_pre_save, sender=Produto)

