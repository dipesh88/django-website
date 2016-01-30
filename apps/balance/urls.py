from django.conf.urls import url

from . import views

#/balance/
urlpatterns = [
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ClearMonthBalanceView.as_view(),name="details"),
    ]