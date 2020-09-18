# Generated by Django 3.0.8 on 2020-09-16 19:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200916_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionfile',
            name='speciality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='speciality_admissions', to='app.Speciality', verbose_name='Spécialité'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.UUID('1bbc9c82-1093-475f-bb19-2d7c657a4678')),
        ),
    ]
