# Generated by Django 4.1 on 2022-09-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_remove_client_city_remove_client_official_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_still_client',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='official_name',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='comment',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
