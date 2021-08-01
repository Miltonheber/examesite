from django.db import models

# Create your models here.


class Post(models.Model):
    data = models.DateTimeField('Data',auto_now_add=True)
    actualizado = models.DateTimeField('actualizado',auto_now=True)
    titulo = models.CharField('Título', max_length=100)
    imagem = models.FileField('imagem',blank=True,upload_to='imagem')
    corpo = models.TextField('Corpo')


    def __str__(self):
        return self.titulo

class Exame(models.Model):
    ano = models.CharField('Ano',max_length=4)
    disciplina = models.CharField('Disciplina',max_length=100)
    instituicao = models.CharField('Instituição',max_length=100)
    nivel = models.CharField('Nivel', max_length=100)
    pdf = models.FileField('arquivo_pdf', upload_to='pdf')

    def __str__(self):
        return self.disciplina


