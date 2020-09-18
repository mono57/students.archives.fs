# Generated by Django 3.0.8 on 2020-09-17 00:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200916_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='short_name',
        ),
        migrations.AddField(
            model_name='verbalproces',
            name='student_list',
            field=models.FileField(blank=True, null=True, upload_to='students/', verbose_name='Fichier étudiants'),
        ),
        migrations.AlterField(
            model_name='level',
            name='full_name',
            field=models.CharField(help_text='Exemple: Niveau 1', max_length=150, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.UUID('6d097c0f-25bb-49ad-aded-fd638897f590')),
        ),
    ]
