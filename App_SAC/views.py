from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def abre_index(request):
    return render(request, 'index.html')

def cad_cliente(request):
    return render(request, 'cad_cliente.html')

def salvar_cliente_novo(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacao = request.POST.get('observacao')
        grava_cliente = Cliente(
            nome=nome,
            telefone=telefone,
            email=email,
            observacao=observacao,
        )
        grava_cliente.save()
        messages.info(request, 'Cliente ' + nome + ' cadastrado com sucesso.')
        return render(request, 'cad_cliente.html')

def cons_cliente(request):
    dado_pesquisa_nome = request.POST.get('cliente')
    dado_pesquisa_telefone = request.POST.get('telefone')
    dado_pesquisa_email = request.POST.get('email')

    if dado_pesquisa_nome != None and dado_pesquisa_nome != '':
        clientes = Cliente.objects.filter(nome__icontains=dado_pesquisa_nome)
        return render(request, 'Cons_Cliente_Lista.html', {'dados_clientes':clientes})

    elif dado_pesquisa_telefone != None and dado_pesquisa_telefone != '':
        clientes = Cliente.objects.filter(telefone__icontains=dado_pesquisa_telefone)
        return render(request, 'Cons_Cliente_Lista.html', {'dados_clientes':clientes})

    elif dado_pesquisa_email != None and dado_pesquisa_email != '':
        clientes = Cliente.objects.filter(email__icontains=dado_pesquisa_email)
        return render(request, 'Cons_Cliente_Lista.html', {'dados_clientes':clientes})

    else:
        return render(request, 'Cons_Cliente_Lista.html')
    

def edit_cliente(request, id):
    dados_editar = get_object_or_404(Cliente, pk=id)
    return render(request, 'Edit_Cliente.html', {'dados_do_cliente': dados_editar})


def salvar_cliente_editado(request):
    if (request.method == 'POST'):
        id_cliente = request.POST.get('id_cliente')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacao = request.POST.get('observacao')

        Cliente_Editado = Cliente.objects.get(id=id_cliente)

        Cliente_Editado.nome = nome
        Cliente_Editado.telefone = telefone
        Cliente_Editado.email = email
        Cliente_Editado.observacao = observacao

        Cliente_Editado.save()

        messages.info(request, 'Cliente ' + nome + ' editado com sucesso.')
        return render(request, 'Cons_Cliente_Lista.html')
    

def delete_cliente(request, id):
    cliente_deletado = get_object_or_404(Cliente, pk=id)
    nome = cliente_deletado.nome
    cliente_deletado.delete()

    messages.info(request, 'Cliente ' + nome + ' excluido com sucesso.')
    return redirect('cons_cliente')
