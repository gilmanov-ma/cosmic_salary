# Generated by Django 4.1 on 2022-10-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0009_alter_payment_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='date_time',
            field=models.DateField(),
        ),
    ]
