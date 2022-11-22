from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name_department = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name_department}'


class Employee(models.Model):
    TYPE_CHOICES = [
        ('Старая', 'Старая'),
        ('Новая', 'Новая'),
    ]
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    post_name = models.CharField(max_length=40)
    department_id = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    comment = models.CharField(max_length=200, default=None, blank=True)
    motivation_type = models.CharField(max_length=40, default=TYPE_CHOICES[1][1], null=True, blank=True,
                                       choices=TYPE_CHOICES)

    def get_url_employees(self):
        return reverse('employee_detail', args=[self.pk])

    def get_id_to_update(self):
        return reverse('update_employee', args=[self.pk])

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.post_name}'


class Client(models.Model):
    STATUS_CHOICES = [
        ('Работаем', 'Работаем'),
        ('Не работаем', 'Не работаем'),
        ('Непонятно', 'Непонятно'),
    ]
    client_name = models.CharField(max_length=40)
    official_name = models.CharField(max_length=40, null=True, default=None)
    city = models.CharField(max_length=40, null=True, default=None)
    is_still_client = models.CharField(max_length=40, choices=STATUS_CHOICES)

    def get_url_clients(self):
        return reverse('client_detail', args=[self.pk])

    def get_id_to_update(self):
        return reverse('update_client', args=[self.pk])

    def __str__(self):
        return f'{self.client_name}'

class Cash(models.Model):
    SERVICES = [
        ('--КУ Стартап--', 'КУ Стартап'),
        ('--КУ Бизнес--', 'КУ Бизнес'),
        ('--КУ Мероприятия--', 'КУ Мероприятия'),
        ('Другое', 'Другое'),
    ]

    date_time = models.DateField(blank=False)
    income = models.PositiveIntegerField(blank=False)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT, default=None, blank=False)
    income_item = models.CharField(max_length=40, blank=False, choices=SERVICES)

    def get_id_to_update(self):
        return reverse('update_cash', args=[self.pk])

    def get_url_cash(self):
        return reverse('cash_detail', args=[self.pk])

    def __str__(self):
        return f'{self.date_time} - {self.income} {self.income_item} {self.client_id}'


class Payment(models.Model):
    date_time = models.DateField(blank=False)
    payment = models.PositiveIntegerField(blank=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.PROTECT, default=None, blank=False)
    comment = models.CharField(max_length=200, null=True, default='Выплата с поступления', blank=True)

    def get_id_to_update(self):
        return reverse('update_payment', args=[self.pk])

    def __str__(self):
        return f'{self.date_time} - {self.payment} {self.employee_id}'
