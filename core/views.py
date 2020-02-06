from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


# Create your views here.

#retorna a renderização do request
def index(request):
    #print(f'Usuário: {request.user}')
    context = {
        #buscando todos os produtos cadastrados
        'produtos':Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    #Esse form pode conter dados ou não
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        #retorna true se formulário não tem erros
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')


    context = {
        'form': form
    }
    #envia para o contexto do template o form
    return render(request, 'contato.html', context)


def produto(request):
    print(f'Usuário: {request.user}')
    if str(request.user) != 'AnonymousUser':
        # se um usuário enviou um form vai ser um request.post e request.FILES por causa da imagem
        if str(request.method) == 'POST':
            #vai vir o arquivo no files
            form = ProdutoModelForm(request.POST, request.FILES)
            # verificar se produto é valido
            if form.is_valid():
                #Salva os dados, mas antes chama o pre_save lá no models
                prod = form.save()
                print(f'Nome: {prod.nome}')
                print(f'Preço: {prod.preco}')
                print(f'Estoque: {prod.estoque}')
                print(f'Imagem: {prod.imagem}')
                messages.success(request, 'Produto salvo com sucesso.')
                # instancia um novo formulário e limpa os dados
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        #apenas carrega o formulário
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')


