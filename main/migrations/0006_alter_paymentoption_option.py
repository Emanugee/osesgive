# Generated by Django 4.1.2 on 2022-10-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_paymentoption_alter_payment_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentoption',
            name='option',
            field=models.CharField(max_length=100),
        ),
    ]
