import django_filters
from django_filters import CharFilter
from .models import *


class AccontFilter(django_filters.FilterSet):
	class Meta:
		model = Account
		fields = {'job': ['icontains']}