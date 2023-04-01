from django.db import models

class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='uploads/%Y/%m/%d/')
