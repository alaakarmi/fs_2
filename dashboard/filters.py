from main.models import Request
import django_filters
from django_filters import DateFilter
from django.forms.widgets import DateInput


class RequestFilter(django_filters.FilterSet):
    date = DateFilter('date_added__date', label='Date', widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Request
        fields = ['department', 'date']