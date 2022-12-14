from audioop import add
from tkinter import N
from typing import Set
from django.shortcuts import render
from django.http import HttpResponse            
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_crm
from django.contrib.auth.decorators import login_required
from .models import Create_CRM
from registration.models import CustomUser, Setor


@login_required(login_url='/')
def createcrm(request):

    if request.method == "GET":
        return render(request, 'createcrm.html', context={
            "setores" : Setor.objects.values,
            'setor' : Setor.objects
        })
    else:
        solicitante = request.user
        data = request.POST.get('data')
        empresa = request.POST.get('empresa')
        versao = request.POST.get('versao')
        file = request.FILES.get('upload')
        setores = request.POST.getlist('setores')
        descricao = request.POST.get('descricao')
        justificativa = request.POST.get('justificativa')
        objetivo = request.POST.get('objetivo')


        crm = Create_CRM.objects.create(solicitante=solicitante, data_criacao=data, empresa=empresa, versao=versao, 
        file=file, descricao=descricao, justificativa=justificativa, objetivo=objetivo)
        
        for x in setores:
            crm.setor.add(x)

        crm.save()

        return render(request, 'home.html')
    



    