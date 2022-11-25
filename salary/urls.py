from django.urls import path
from .views import main_menu, OneCLient, AllEmployees, AllCLients, \
    OneEmployee, AllCash, UpdateFormClient, CreateFormClient, CreateFormEmployee, UpdateFormEmployee,\
    UpdateFormCash, CreateFormCash, UpdateFormPayEmployee, CreateFormPayEmployee, AllPayments, home_view, OneCash, \
    ChangeStatus

urlpatterns = [
    path('', main_menu, ),
    path('clients', AllCLients.as_view(), name='all_clients'),
    path('clients/<int:id_client>', OneCLient.as_view(),  name='client_detail'),
    path('employees/<int:id_employee>', OneEmployee.as_view(),  name='employee_detail'),
    path('cash/<int:id_cash>', OneCash.as_view(), name='cash_detail'),
    path('employees', AllEmployees.as_view(), name='all_employees'),
    path('cash', AllCash.as_view(), name='all_cash'),
    path('payment_calendar', AllCash.as_view(), name='payment_calendar'),
    path('payments', AllPayments.as_view(), name='all_payments'),
    path('update/<int:pk>', UpdateFormClient.as_view(), name='update_client'),
    path('add_client', CreateFormClient.as_view()),
    path('add_employee', CreateFormEmployee.as_view()),
    path('add_payment', CreateFormPayEmployee.as_view()),
    path('edit_employee/<int:pk>', UpdateFormEmployee.as_view(), name='update_employee'),
    path('add_cash', CreateFormCash.as_view()),
    path('edit_cash/<int:pk>', UpdateFormCash.as_view(), name='update_cash'),
    path('edit_payment/<int:pk>', UpdateFormPayEmployee.as_view(), name='update_payment'),
    path('edit_status/<int:id_payment>', ChangeStatus.as_view(), name='change_status'),
    path('home_view', home_view),
]
