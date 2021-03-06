import django_filters

from .models import Task

class NullFilter(django_filters.BooleanFilter):
	"""Filter on a field set as null or not."""

	def filter(self, qs, value):
		if value is not None:
			return qs.filter(**{'{}__isnull'.format(self.name): value })
		return qs


class TaskFilter(django_filters.FilterSet):

	backlog = NullFilter(name='sprint')

	class Meta:
		model = Task
		fields = ('sprint', 'status', 'assigned', 'backlog',)


