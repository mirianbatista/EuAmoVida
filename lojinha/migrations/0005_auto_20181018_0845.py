# Generated by Django 2.1 on 2018-10-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojinha', '0004_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
