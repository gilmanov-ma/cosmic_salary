# Generated by Django 4.1 on 2022-09-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0004_alter_client_city_alter_client_official_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_still_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='official_name',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
    ]
