from django.conf.urls import include, url

from . import views

#/expenses/
urlpatterns = [
    url(r'^(?P<pk>[0-9])/(?P<slug>[-\w]+)/$', views.ExpenseView.as_view(),name='details'),
    url(r'^add/$', views.AddExpenseView.as_view(),name='add'),
    
    
]