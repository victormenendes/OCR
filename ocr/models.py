from django.db import models
import os
def caminho_arquivo(instance, filename):
    return os.path.join('uploads', filename)


class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='caminho_arquivo')
