from django.template import Library
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

register = Library()

@register.inclusion_tag('pagination.html')
def pagination(request, pagination, page_obj):
	context = {}
	context['paginator'] = paginator
	context['request'] = request
	context['page_obj'] = page_obj
	return context