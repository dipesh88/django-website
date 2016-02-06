from django.core.paginator import Paginator
from django.conf import settings

def update_pagination_context(request,context,object_list):
    
    if len(object_list) > settings.MAX_PAGINATION_ITEMS_PER_PAGE:
        context['paginate'] = True
        p = Paginator(object_list,settings.MAX_PAGINATION_ITEMS_PER_PAGE)
        page = p.page(int(request.GET.get('page',1)))
        context['page'] = page
        context['pages'] = p.page_range
        context['object_list'] = page.object_list
    
    return