# Generated by Django 4.2 on 2023-07-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_management', '0010_loan_amount_with_interest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanplan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
