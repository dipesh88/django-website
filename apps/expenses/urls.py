from django.conf.urls import include, url

from . import views

#/expenses/
urlpatterns = [
    url(r'^(?P<pk>[0-9])/(?P<slug>[-\w]+)/$', views.ExpenseView.as_view(),name='details'),
    url(r'^add/$', views.AddExpenseView.as_view(),name='add'),
    url(r'^edit/(?P<pk>[0-9])/(?P<slug>[-\w]+)/$', views.EditExpenseView.as_view(),name='edit'),
    url(r'^approve/(?P<pk>[0-9])/(?P<slug>[-\w]+)/$', views.ApproveExpenseView.as_view(),name='approve'),
    
    
]