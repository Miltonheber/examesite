from django.shortcuts import render,get_object_or_404, redirect

from .models import Post, Exame

# Create your views here.
def index(request):
    objecto = Post.objects.all()
    contexto = {'postagem':objecto}
    return render(request, 'index.html',contexto)

def sobre(request):
    return render(request, 'sobre.html')



	
def exame_matematica(request):
    objecto = Exame.objects.filter(disciplina='matematica',nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'matematica.html',contexto)
	
'''def exame_fisica(request):
    objecto = Exame.objects.filter(disciplina=fisica)
    contexto = {'exames':objecto}
	return render(request, 'fisica.html', contexto)'''
	
def exame_quimica(request):
    objecto = Exame.objects.filter(disciplina='quimica', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'quimica.html',contexto)
def exame_fisica(request):
    objecto = Exame.objects.filter(disciplina='fisica', nivel='superior')
    contexto={'exames':objecto}
    return render(request, 'fisica.html',contexto)
	

def exame_etp(request):
    objecto = Exame.objects.filter(nivel='medio')
    contexto = {'exames':objecto}
    return render(request, 'etp.html', contexto)
	

def exame_escolar(request):
    objecto = Exame.objects.filter(nivel='escolar')
    contexto = {'exames':objecto}
    return render(request, 'exame_escolar.html',contexto)
	
def outros_exames(request):
    objecto = Exame.objects.filter(disciplina='outros_exames')
    contexto = {'exames':objecto}
    return render(request, 'outros_exames.html')
	
def error404(request, exception):
    return render(request, 'error404.html')

def error500(request):
    return render(request, 'error500.html')

def postagem(request, id):
    objecto = get_object_or_404(Post, id=id)
    contexto ={'postagem':objecto}
    return render(request, 'postagem.html', contexto)

def exame_portugues(request):
    objecto = Exame.objects.filter(disciplina='portugues', nivel='superior')
    contexto = {'exames':objecto}
    return render(request, 'portugues.html', contexto)


	

