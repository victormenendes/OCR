from .forms import ArquivoForm
import os
import PyPDF2


from django.shortcuts import render

def index(request):
    return render(request, 'base.html')


def upload_arquivo(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            caminho_arquivo = 'media/' + arquivo.name
            with open(caminho_arquivo, 'wb+') as destino:
                for chunk in arquivo.chunks():
                    destino.write(chunk)

            texto = extrair_texto(caminho_arquivo)
            os.remove(caminho_arquivo)
            return render(request, 'resultado.html', {'texto': texto})
    else:
        form = ArquivoForm()
    return render(request, 'formulario.html', {'form': form})


def extrair_texto(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as arquivo:
        leitor_pdf = PyPDF2.PdfReader(arquivo)
        num_paginas = len(leitor_pdf.pages)
        texto = ''
        for pagina in range(num_paginas):
            texto += leitor_pdf.pages[pagina].extract_text()
    return texto





