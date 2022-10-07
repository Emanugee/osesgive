# Generated by Django 4.1.2 on 2022-10-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_payment_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='purpose',
            field=models.CharField(choices=[('Offering', 'Offering'), ('Tithe', 'Tithe'), ('Thanksgiving', 'Thanksgiving'), ('Transport', 'Transport'), ('Project 22', 'Project 22'), ('Shiloh Sacrifice', 'Shiloh Sacrifice'), ('Welfare', 'Welfare'), ('Prophet Offering', 'Prophet Offering')], max_length=100),
        ),
    ]