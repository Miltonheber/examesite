# Generated by Django 3.2.5 on 2021-07-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4, verbose_name='Ano')),
                ('disciplina', models.CharField(max_length=100, verbose_name='Disciplina')),
                ('instituicao', models.CharField(max_length=100, verbose_name='Instituição')),
                ('nivel', models.CharField(max_length=100, verbose_name='Nivel')),
                ('pdf', models.FileField(upload_to='pdf', verbose_name='arquivo_pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('imagem', models.FileField(blank=True, upload_to='imagem', verbose_name='imagem')),
                ('corpo', models.TextField(verbose_name='Corpo')),
            ],
        ),
    ]