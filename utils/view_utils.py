import datetime
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.safestring import mark_safe


def update_pagination_context(request,context,object_list):
    
    if len(object_list) > settings.MAX_PAGINATION_ITEMS_PER_PAGE:
        context['paginate'] = True
        p = Paginator(object_list,settings.MAX_PAGINATION_ITEMS_PER_PAGE)
        page = p.page(int(request.GET.get('page',1)))
        context['page'] = page
        context['pages'] = p.page_range
        context['object_list'] = page.object_list
    
    return




class ModelToHtml(object):
    """ html output for fields by verbose name, in the order provided"""
    
    row_template =  "{row_start} {label} {divider} {value} {row_end} \n"
    obj = None
    
    def __init__(self,model,fields):
        
        self.model = model
        self.Lfields = fields
        s = set(model._meta.get_all_field_names())
        assert set(fields).issubset(s)
             
    def _row(self,field_name,value,row_start,row_end, divider=":"):
        
        label = self.model._meta.get_field(field_name).verbose_name
        return self.row_template.format(row_start=row_start,label=label,row_end=row_end,divider=divider,value=value)
        
    def as_p(self):
        
        html_output = ""
        for field_name in self.Lfields:
            value = getattr(self.obj,field_name)
            if isinstance(value,datetime.datetime):
                value = value.strftime("%Y-%m-%d %H:%M")
            else:
                value = str(value)
            
            html_output = html_output + self._row(field_name,value,"<p>","</p>")
            
        return mark_safe(html_output)
    
    
class ModelToHtmlMixin(object):
    
    model_to_html_fields = None
    model_to_html = None
    
    def __init__(self,*args,**kwargs):
        
        self.model_html = ModelToHtml(self.model_to_html, self.model_to_html_fields)
    
    def get_context_data(self,*args,**kwargs):
        
        context = super(ModelToHtmlMixin,self).get_context_data(*args,**kwargs)
        self.model_html.obj = self.object
        context ['model_html'] = self.model_html
        return context
        
            
            
            
        
        
            
        
        
        
        
        
        