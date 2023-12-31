# Generated by Django 4.2 on 2023-07-21 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_management', '0002_loanplan_remove_loancustomer_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_management.loancustomer'),
        ),
        migrations.AlterField(
            model_name='loanfund',
            name='loan_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_management.loanprovider'),
        ),
    ]
