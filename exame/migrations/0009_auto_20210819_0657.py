# Generated by Django 3.2.5 on 2021-08-19 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0008_auto_20210816_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='post',
            name='texto',
        ),
    ]