# Generated by Django 4.2.4 on 2024-03-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_genter_alter_newproducts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genter',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='Men', max_length=200),
        ),
    ]