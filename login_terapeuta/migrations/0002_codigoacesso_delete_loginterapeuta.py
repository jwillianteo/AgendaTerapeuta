# Generated by Django 5.1.2 on 2024-11-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_terapeuta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('usado', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='LoginTerapeuta',
        ),
    ]
