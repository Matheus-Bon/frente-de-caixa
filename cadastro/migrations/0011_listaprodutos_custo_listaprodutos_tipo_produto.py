# Generated by Django 4.1.3 on 2022-11-12 23:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_alter_listaprodutos_nota_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaprodutos',
            name='custo',
            field=models.FloatField(default=datetime.datetime(2022, 11, 12, 23, 49, 5, 774161, tzinfo=datetime.timezone.utc), verbose_name='Custo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listaprodutos',
            name='tipo_produto',
            field=models.TextField(default=datetime.datetime(2022, 11, 12, 23, 49, 14, 815211, tzinfo=datetime.timezone.utc), verbose_name='Tipo de Produto'),
            preserve_default=False,
        ),
    ]