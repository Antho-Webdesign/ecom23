# Generated by Django 4.1.5 on 2023-01-14 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_ttc',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='images/store/products/default.png', null=True, upload_to='images/store/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='marque_produit',
            field=models.CharField(max_length=120),
        ),
    ]