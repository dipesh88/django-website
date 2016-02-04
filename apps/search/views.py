from django.http import Http404
from django.shortcuts import render
from django.views import generic

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
        
        
    