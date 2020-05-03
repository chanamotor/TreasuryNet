from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dashboard/', views.Dashboard,name='finance_dashboard'),
    path('budget-entry/', views.budget_form,name='finance_budgetentry'),
    path('<int:id>/', views.budget_form,name = 'finance_budgetupdate' ),
    path('delete/<int:id>/',views.budget_delete,name='finance_budgetdelete'),
    path('list/',views.budget_list,name='finance_budgetlist') # get req. to retrieve and display all records
]
