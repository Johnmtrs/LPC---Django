# Generated by Django 2.1.7 on 2019-03-16 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128, verbose_name='Título')),
                ('conteudo', models.TextField()),
                ('data_cria', models.DateTimeField(verbose_name='Data criação')),
                ('data_pub', models.DateField(auto_now=True)),
                ('publicado', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
    ]
