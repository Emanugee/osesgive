# Generated by Django 4.1.2 on 2022-10-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cart_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
