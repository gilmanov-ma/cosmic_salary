import django_filters
from .models import Cash, Payment
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class CashFilter(django_filters.FilterSet):
    client_id__client_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cash
        fields = {'date_time': ['gt', 'lt'], 'income_item': ['contains'], }

class PaymentFilter(django_filters.FilterSet):
    employee_id__last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Payment
        fields = {'date_time': ['gt', 'lt'], }



