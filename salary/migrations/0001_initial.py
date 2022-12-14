# Generated by Django 4.1 on 2022-09-22 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=40)),
                ('official_name', models.CharField(default=None, max_length=60, null=True)),
                ('city', models.CharField(default=None, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_department', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('post_name', models.CharField(max_length=40)),
                ('comment', models.CharField(default=None, max_length=200, null=True)),
                ('department_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='salary.department')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('payment', models.PositiveIntegerField()),
                ('employee_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='salary.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('income', models.PositiveIntegerField()),
                ('income_item', models.CharField(max_length=40)),
                ('outcome', models.PositiveIntegerField(blank=True, default=False)),
                ('client_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='salary.client')),
                ('payment_to', models.ManyToManyField(to='salary.employee')),
            ],
        ),
    ]
