# Generated by Django 2.0 on 2023-10-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('funcao', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
    ]