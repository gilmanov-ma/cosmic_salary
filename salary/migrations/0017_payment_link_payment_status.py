# Generated by Django 4.1.3 on 2022-11-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0016_remove_cash_payment_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Оплачено', 'Оплачено'), ('На проверке', 'На проверке')], default='На проверке', max_length=40),
        ),
    ]