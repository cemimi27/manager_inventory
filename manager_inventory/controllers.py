import sys

from django.shortcuts import HttpResponse, render


def validarLogin(request):
    # ATRIBUI O VALOR DO ATRIBUTO NAME DA REQUISIÇÃO POST NA VARIÁVEL USUÁRIO
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    if len(usuario) == 0:
        return HttpResponse('ErroUsuarioVazio')
        sys.exit
    if len(senha) == 0:
        return HttpResponse('ErroSenhaVazio')
        sys.exit
    return HttpResponse('Sucesso')
