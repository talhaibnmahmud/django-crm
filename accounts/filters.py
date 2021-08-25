import django_filters
from django_filters import CharFilter, DateFilter

from accounts import models


class OrderFilter(django_filters.FilterSet):
    """docstring for OrderFilter"""
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        """docstring for Meta"""
        model = models.Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
