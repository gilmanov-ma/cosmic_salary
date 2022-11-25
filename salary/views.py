from django.shortcuts import render, get_object_or_404, reverse
from .models import Client, Employee, Cash, Payment
from .forms import AddEmployee, AddCash, AddClient, AddPayment, AccountsListForm, MarketersListForm, EditStatusClient, \
    EditStatusPayment
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import UpdateView, CreateView
from .filters import CashFilter, PaymentFilter
import datetime


Motivation = dict(account_old_motivation=0.5, account_new_motivation=0.4)


''' Вызывает главное меню'''
def main_menu(request):
    return render(request, 'salary/main.html', )


class AllCLients(View):
    """ Показывает страницу со всеми клиентами"""
    def get(self, request):
        form = AddClient()
        clients = Client.objects.all()
        context = {'clients': clients, 'form': form, }
        return render(request, 'salary/all_clients.html', context=context)

    def post(self, request):
        form = AddClient(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clients')


class OneCLient(View):
    """ Показывает страницу с детализацией клиента"""
    def get(self, request, id_client):
        form = EditStatusClient()
        client = get_object_or_404(Client, id=id_client)
        context = {'client': client, 'form': form, }
        return render(request, 'salary/one_client.html', context=context)

    def post(self, request, id_client):
        client_instance = Client.objects.get(pk=id_client)
        form = EditStatusClient(request.POST, instance=client_instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/clients')


class OneEmployee(View):
    """ Показывает страницу с детализацией сотрудника"""
    def get(self, request, id_employee):
        form = AddPayment()
        payments = Payment.objects.filter(employee_id=id_employee)
        employee = get_object_or_404(Employee, id=id_employee)
        payment_filter = PaymentFilter(request.GET, queryset=payments)
        context = {'employee': employee, 'payments': payments, 'form': form, 'payment_filter': payment_filter}
        return render(request, 'salary/one_employee.html', context=context)

class ChangeStatus(View):
    """ Показывает форму с подтверждением для оплаты"""
    def get(self, request, id_payment):
        form = EditStatusPayment()
        payment = get_object_or_404(Payment, id=id_payment)
        context = {'payment': payment, 'form': form, }
        return render(request, 'salary/change_status_form.html', context=context)

    def post(self, request, id_payment):
        payment_instance = Payment.objects.get(pk=id_payment)
        form = EditStatusPayment(request.POST, instance=payment_instance)
        id_employee = payment_instance.employee_id.pk
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('employee_detail', args=(id_employee,)))

class OneCash(View):
    """ Показывает страницу с детализацией платежа"""
    def get(self, request, id_cash):
        form_list_accounts = AccountsListForm()
        cash = get_object_or_404(Cash, id=id_cash)
        context = {'cash': cash, 'form_list_accounts': form_list_accounts}
        return render(request, 'salary/one_cash.html', context=context)

    def post(self, request, id_cash):
        form_list_accounts = AccountsListForm(request.POST)
        if form_list_accounts.is_valid():
            employee_id = form_list_accounts.cleaned_data['account_manager']
            if Employee.objects.filter(pk=employee_id)[0].motivation_type == 'Новая':
                payment = Cash.objects.filter(pk=id_cash)[0].income * Motivation['account_new_motivation']
            else:
                payment = Cash.objects.filter(pk=id_cash)[0].income * Motivation['account_old_motivation']

            Payment.objects.create(
                date_time=datetime.date.today(),
                employee_id=Employee.objects.filter(pk=employee_id)[0],
                payment=payment,
                comment='Выплата с поступления'
            )
            return render(request, 'salary/success_message.html')
        else:
            return render(request, 'salary/error_message.html')


class AllEmployees(View):
    """ Показывает страницу со всеми сотрудниками"""
    def get(self, request):
        form = AddEmployee()
        employees = Employee.objects.all()
        context = {'employees': employees, 'form': form}
        return render(request, 'salary/all_employees.html', context=context)

    def post(self, request):
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
        else:
            return render(request, 'salary/error_message.html')


class AllCash(View):
    """ Показывает страницу со всеми поступлениями"""
    def get(self, request):
        form = AddCash()
        cashes = Cash.objects.all()
        form_list_accounts = AccountsListForm()
        form_list_marketers = MarketersListForm()
        cash_filter = CashFilter(request.GET, queryset=cashes)
        context = {'cashes': cashes, 'form': form, 'cash_filter': cash_filter,\
                   'form_list_accounts': form_list_accounts, 'form_list_marketers': form_list_marketers,
                   }
        return render(request, 'salary/all_cash.html', context=context)

    def post(self, request):
        form = AddCash(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cash')
        else:
            return render(request, 'salary/error_message.html')


class AllPayments(View):
    """ Показывает страницу со всеми расходами"""
    def get(self, request):
        form = AddPayment()
        payments = Payment.objects.all()
        payment_filter = PaymentFilter(request.GET, queryset=payments)
        context = {'payments': payments, 'form': form, 'payment_filter': payment_filter, }
        return render(request, 'salary/all_payments.html', context=context)

    def post(self, request):
        form = AddPayment(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/payments')
        else:
            return render(request, 'salary/error_message.html')


class UpdateFormClient(UpdateView):
    """ Редактирование формы клиента"""
    model = Client
    form_class = AddClient
    template_name = 'salary/edit_client_form.html'
    success_url = '/clients'


class CreateFormClient(CreateView):
    """ Создание формы клиента"""
    model = Client
    form_class = AddClient
    template_name = 'salary/add_client_form.html'
    success_url = '/clients'


class UpdateFormEmployee(UpdateView):
    """ Редактирование формы сотрудника"""
    model = Employee
    form_class = AddEmployee
    template_name = 'salary/edit_employee_form.html'
    success_url = '/employees'


class CreateFormEmployee(CreateView):
    """ Создание формы сотрудника"""
    model = Employee
    form_class = AddEmployee
    template_name = 'salary/add_employee_form.html'
    success_url = '/employees'


class UpdateFormCash(UpdateView):
    """ Редактирование формы поступления"""
    model = Cash
    form_class = AddCash
    template_name = 'salary/edit_cash.html'
    success_url = '/cash'


class CreateFormCash(CreateView):
    """ Создание формы поступления"""
    model = Cash
    form_class = AddCash
    template_name = 'salary/add_cash.html'
    success_url = '/cash'


class UpdateFormPayEmployee(UpdateView):
    """ Редактирование формы оплаты сотруднику"""
    model = Payment
    form_class = AddPayment
    template_name = 'salary/edit_payment.html'
    success_url = '/employees'

class CreateFormPayEmployee(CreateView):
    """ Создание формы оплаты сотруднику"""
    model = Payment
    form_class = AddPayment
    template_name = 'salary/add_payment.html'
    success_url = '/employees'


def home_view(request):
    """Функция для тестирования"""
    context = {}
    context["form"] = AccountsListForm()
    return render(request, "salary/listform.html.", context)