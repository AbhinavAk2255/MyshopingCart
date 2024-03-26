# Generated by Django 4.2.4 on 2024-03-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newproducts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
                ('new_price', models.FloatField()),
                ('old_price', models.FloatField()),
            ],
        ),
    ]
