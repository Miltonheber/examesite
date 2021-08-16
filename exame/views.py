from django.shortcuts import render,get_object_or_404, redirect
from .forms import ContactoForm
from django.contrib import messages
from .models import Post, Exame

# Create your views here.
def contacto(request):
    form = ContactoForm()
    contexto = {'form':form}
    if str(request.method)=='POST':
        if form.is_valid():
            print('oky')
    return render(request, 'contacto.html', contexto)

def index(request):
    objecto = Post.objects.all()
    contexto = {'postagem':objecto}
    return render(request, 'index.html',contexto)

def privacidade(request):
    return render(request, 'sobre.html')

def sobre(request):
    return render(request, 'sobre1.html')



	
def exame_matematica(request):
    objecto = Exame.objects.filter(disciplina='matematica',nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'matematica.html',contexto)
	
def exame_quimica(request):
    objecto = Exame.objects.filter(disciplina='quimica', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'quimica.html',contexto)
def exame_fisica(request):
    objecto = Exame.objects.filter(disciplina='fisica', nivel='superior')
    contexto={'exames':objecto}
    return render(request, 'fisica.html',contexto)
	

def exame_etp(request):
    objecto1 = Exame.objects.filter(nivel='medio', disciplina='fisica')
    objecto2 = Exame.objects.filter(nivel='medio', disciplina='portugues')
    objecto3 = Exame.objects.filter(nivel='medio', disciplina='matematica')
    contexto = {
            'fisica':objecto1,
            'portugues':objecto2,
            'matematica':objecto3
            }
    return render(request, 'etp.html', contexto)
	

def exame_escolar(request):
    obj1= Exame.objects.filter(nivel='escolar',disciplina='portugues')
    obj2= Exame.objects.filter(nivel='escolar',disciplina='matematica')
    obj3 = Exame.objects.filter(nivel='escolar',disciplina='desenho')
    obj4 = Exame.objects.filter(nivel='escolar', disciplina='quimica')
    obj5 = Exame.objects.filter(nivel='escolar',disciplina='fisica')
    obj6 = Exame.objects.filter(nivel='escolar', disciplina='english')
    obj7 = Exame.objects.filter(nivel='escolar', disciplina='geografia')
    obj8 = Exame.objects.filter(nivel='escolar', disciplina='historia')

    contexto ={
            'fisicas':obj5,
            'matematicas':obj2,
            'portuguess':obj1,
            'desenhos':obj3,
            'quimicas':obj4,
            'englishs':obj6,
            'geografias':obj7,
            'historias':obj8
            }

    return render(request, 'exame_escolar.html', contexto)

	
def outros_exames(request):
    objecto = Exame.objects.filter(disciplina='outros_exames')
    contexto = {'exames':objecto}
    return render(request, 'outros_exames.html')
	
def error404(request, exception):
    return render(request, 'error404.html')

def error500(request):
    return render(request, 'error500.html')

def postagem(request, id):
    obj = Post.objects.filter(alta=True)
    objecto = get_object_or_404(Post, id=id)
    contexto ={'postagem':objecto, 'posts':obj}
    return render(request, 'postagem.html', contexto)

def exame_portugues(request):
    objecto = Exame.objects.filter(disciplina='portugues', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'portugues.html', contexto)


def exame_geografia(request):
    objecto = Exame.objects.filter(disciplina='geografia', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'geografia.html', contexto)


def exame_historia(request):
    objecto = Exame.objects.filter(disciplina='historia', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'historia.html', contexto)


def exame_english(request):
    objecto = Exame.objects.filter(disciplina='english', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'english.html', contexto)

