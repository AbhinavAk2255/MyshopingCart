# Generated by Django 4.2.4 on 2024-03-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_genter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genter',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], max_length=200),
        ),
    ]
