# Generated by Django 3.0.8 on 2021-07-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=40)),
                ('idade', models.IntegerField()),
                ('nascimento', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('apelido', models.CharField(max_length=50)),
                ('observacao', models.CharField(max_length=100)),
            ],
        ),
    ]
