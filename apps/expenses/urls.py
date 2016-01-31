from django.conf.urls import include, url

from . import views

#/expenses/
urlpatterns = [
    
    url(r'^$', views.MainExpensesRedirectView.as_view(),name='details'),
    
    # expense
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[-\w]+)/$', views.ExpenseView.as_view(),name='details'),
    url(r'^add/$', views.AddExpenseView.as_view(),name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/(?P<slug>[-\w]+)/$', views.EditExpenseView.as_view(),name='edit'),
    url(r'^approve/(?P<pk>[0-9]+)/(?P<slug>[-\w]+)/$', views.ApproveExpenseView.as_view(),name='approve'),
    
    # list views
    # GET arg ?approve=yes/no/all
    url(r'^monthly/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.MonthlyExpensesAllView.as_view(),name='monthly_all'),
    url(r'^monthly/my/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.MonthlyExpensesMyView.as_view(),name='monthly_my'),
    url(r'^monthly/divorcee/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.MonthlyExpensesDivorceeView.as_view(),name='monthly_divorcee'),
    
    
]