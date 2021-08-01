from django.contrib import admin
from .models import Post, Exame

# Register your models here.
class customizadopost(admin.ModelAdmin):
	list_display = ('titulo', 'data')

class customizadoexame(admin.ModelAdmin):
	list_display = ('ano', 'disciplina','instituicao')
	

admin.site.register(Post, customizadopost)
admin.site.register(Exame, customizadoexame)
