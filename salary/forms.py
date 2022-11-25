from .models import Employee, Client, Cash, Payment, Department
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class AddClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EditStatusClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['is_still_client']

class EditStatusPayment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['status']

class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AddCash(forms.ModelForm):
    class Meta:
        widgets = {'date_time': DateInput()}
        model = Cash
        fields = '__all__'

class AddPayment(forms.ModelForm):
    class Meta:
        widgets = {'date_time': DateInput()}
        model = Payment
        fields = '__all__'

# creating a form
class AccountsListForm(forms.Form):
    ACCOUNT_CHOICES = (
        Employee.objects.filter(department_id=Department.objects.get(name_department='Аккаунт'))
    )
    account_list = ((elem.pk, elem.last_name) for elem in ACCOUNT_CHOICES)
    account_manager = forms.ChoiceField(choices=account_list)


class MarketersListForm(forms.Form):
    MARKETER_CHOICES = (
        Employee.objects.filter(department_id=Department.objects.get(name_department='Маркетинг')))
    marketer_list = ((count, elem.last_name,) for count, elem in enumerate(MARKETER_CHOICES))
    marketer_manager = forms.ChoiceField(choices=marketer_list)

