# Generated by Django 3.2.5 on 2021-08-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0006_auto_20210814_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='documentos', verbose_name='documento'),
        ),
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Texto do documento'),
        ),
    ]