# Generated by Django 4.1 on 2022-09-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_client_city_client_is_still_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='official_name',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='comment',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]