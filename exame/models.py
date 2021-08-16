from django.db import models

# Create your models here.


class Post(models.Model):
    data = models.DateTimeField('Data',auto_now_add=True)
    actualizado = models.DateTimeField('actualizado',auto_now=True)
    titulo = models.CharField('Título', max_length=100,unique=True)
    imagem = models.FileField('imagem',upload_to='imagem',blank=True)
    corpo = models.TextField('Corpo')
    alta = models.BooleanField(default=False)
    pdf = models.FileField('doc', blank=True, upload_to='documentos')
    texto = models.CharField('texto do doc', max_length=300, blank=True)

    



    class Meta:
        ordering = ['-data',]
     



    def __str__(self):
        return self.titulo

class Exame(models.Model):

    DISCIPLINAS_CHOISES = (
            ('matematica', 'matematica'),
            ('fisica','fisica'),
            ('geografia','geografia'),
            ('portugues','portugues'),
            ('english','english'),
            ('quimica','quimica'),
            ('filosofia','filosofia'),
            ('desenho','desenho')

            )
    NIVEL_CHOISES = (
            ('medio','medio'),
            ('superior','superior'),
            ('escolar','escolar')

            )
    CLASSE_CHOISES = (
            ('12','12'),
            ('10','10')
            )
    UNI_CHOISES =(
            ('UEM', 'Universidade Eduardo Mondlane'),
            ('UP', 'Universidade Pedagógica'),
            ('UJC', 'Univeridade Jaoquim Chissano'),
            ('IFP','IFP'),
            ('ICISA','ICISA'),
            ('Outra','Outra'),
            ('escolar','escolar'),
            ('ETP','ETP')

            )
    ANO_CHOICES = (
           ('2000','2000'),
           ('2001','2001'),
           ('2002','2002'),
           ('2003','2003'),
           ('2004','2004'),
           ('2005','2005'),
           ('2006','2006'),
           ('2007','2007'),
           ('2008','2008'),
           ('2009','2009'),
           ('2010','2010'),
           ('2011','2011'),
           ('2012','2012'),
           ('2013','2013'),
           ('2014','2014'),
           ('2015','2015'),
           ('2016','2016'),
           ('2017','2017'),
           ('2018','2018'),
           ('2019','2019'),
           ('2020','2020'),
           ('2021','2021'),
           ('2022','2022'),
           ('2023','2023'),
           ('2024','2024'),
           ('2025','2025')


           )



    ano = models.CharField('Ano',max_length=4,unique=True, choices=ANO_CHOICES)
    disciplina = models.CharField('Disciplina',max_length=100, choices=DISCIPLINAS_CHOISES)
    instituicao = models.CharField('Instituição',max_length=100, choices=UNI_CHOISES)
    nivel = models.CharField('Nivel', max_length=100, choices=NIVEL_CHOISES)
    pdf = models.FileField('arquivo_pdf', upload_to='pdf', unique=True)
    classe = models.CharField('classe', max_length=100,blank=True,choices=CLASSE_CHOISES)
    class Meta:
        ordering = ['-ano',]

    def __str__(self):
        return self.disciplina


