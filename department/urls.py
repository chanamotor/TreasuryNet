from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('department/dashboard', views.DashboardView.as_view(), name='department_dashboard'),
    path('department/bill-entry', views.BillEntryView.as_view(), name='department_billentry'),
    path('department/view-bill', views.ViewBillView.as_view(), name='department_viewbill'),
]

urlpatterns += [
    path('department/logout/', views.LogoutView.as_view(), name='signout'),
]