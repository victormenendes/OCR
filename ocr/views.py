from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ArquivoForm
import os
import tensorflow as tf
from PIL import Image
import pytesseract

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
    imagem = Image.open(caminho_arquivo)
    texto = pytesseract.image_to_string(imagem, lang='por')
    return texto
