from django.urls import path
from .views import *


urlpatterns = [
        path('', index, name='index'),
        path('matematica',exame_matematica,name='exame_matematica'),
        path('portugues',exame_portugues,name='exame_portugues'),
        path('fisica',exame_fisica,name='exame_fisica'),
        path('quimica',exame_quimica,name='exame_quimica'),
        path('etp',exame_etp,name='exame_etp'),
        path('escolar',exame_escolar,name='exame_escolar'),
        path('outrosexames',outros_exames,name='outros_exames'),
        path('postagem/<int:id>', postagem,name='Postagem'),
        path('sobre', sobre, name='sobre'),




        ]


