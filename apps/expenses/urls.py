from django.conf.urls import include, url

from . import views

#/expenses/
urlpatterns = [
    url(r'^add/$', views.AddExpenseView.as_view(),name='add'),
    
]