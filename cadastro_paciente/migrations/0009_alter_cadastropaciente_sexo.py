# Generated by Django 5.0.4 on 2024-05-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_paciente', '0008_cadastropaciente_terapeuta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastropaciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True),
        ),
    ]
