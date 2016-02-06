from django.http import Http404
from django.shortcuts import render
from django.views import generic

from ...utils.view_utils import update_pagination_context
from .models import SearchItems
from .forms import SearchForm

class SearchView(generic.ListView):
    
    template_name = "search/results.html"
    
    def get_queryset(self):
        
        try:
            q = SearchForm({'search_query':self.request.GET['q']})
            assert q.is_valid()
            queryset = SearchItems.items.search(self.request.user.account,
                                                q.cleaned_data['search_query'])
            return queryset
        
        except:
            raise
        
        
    def get_context_data(self,*args,**kwargs):
        
        context = super(SearchView,self).get_context_data(*args,**kwargs)
        update_pagination_context(self.request,context,self.object_list)
        
        return context
        
    