#é nesse arquivo form que cria todos os formulários

from django import forms
#definindo que esse formulário enviará email
from django.core.mail.message import EmailMessage
from .models import Produto

#herdando de form
class ContatoForm(forms.Form):
    nome = forms.CharField(label = 'Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            #to é uma lista
            to=['contato@seudominio.com.br', ],
            headers={'Reply-To': email}
        )
        #Dispara o e-mail
        mail.send()


#Definição da classe de modelo, esta herdando de model form
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        #ao invés de fazer como acima ele vai pegar os dados e metadados diretamente do modelo de produto
        model = Produto
        # Apresentar os campos para que o usuário informe esses campos
        fields = ['nome', 'preco', 'estoque', 'imagem']
