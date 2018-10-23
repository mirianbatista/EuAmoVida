# Generated by Django 2.1 on 2018-10-23 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lojinha', '0009_remove_produto_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave do carrinho')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojinha.Produto', verbose_name='Produto')),
            ],
        ),
    ]
