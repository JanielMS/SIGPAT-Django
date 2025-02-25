# Generated by Django 5.1.6 on 2025-02-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(default=1, max_length=18, unique=True),
            preserve_default=False,
        ),
    ]
