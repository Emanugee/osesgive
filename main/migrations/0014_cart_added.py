# Generated by Django 4.1.2 on 2022-10-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_payment_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
