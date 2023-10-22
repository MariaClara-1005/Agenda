from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
from django.contrib.auth import logout
import mysql.connector
from datetime import datetime
import random

# Create your views here.
def home (request):
    cadastros = Cadastro.objects.all().order_by('nome')
    return render(request, 'index.html', {'cadastros': cadastros})

def cadastro (request):
    msg = ""
    if request.method == "POST":
        nome = request.POST.get('nome')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        funcao = request.POST.get('funcao')
        descricao = request.POST.get('descricao')
        Cadastro(nome=nome, tel=tel, email=email, funcao=funcao, descricao=descricao).save()
        msg = "Salvo!"
    return render(request, 'cadastro.html', {'msg': msg})

def delCadastro(request, cod):
    Cadastro.objects.filter(id=cod).delete()
    return redirect(home)

def consultaCadastro(request, cod):
    cadastro = Cadastro.objects.filter(id=cod)
    return render(request, 'consultaCadastro.html', {'cadastro': cadastro})
