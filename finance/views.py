from django.shortcuts import render
from django.shortcuts import render,redirect
from payment.models import BudgetMaster
from .forms import BudgetForm
from django.contrib.auth.models import auth
from django.contrib import messages
from django.utils.crypto import get_random_string
# Create your views here.

def Dashboard(request):
    return render(request, "pages/finance/dashboard.html")

def budget_list(request):
    context = {'budget_list': BudgetMaster.objects.all()}
    return render(request, "pages/finance/budget_list.html", context)


def budget_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BudgetForm()
        else:
            budget = BudgetMaster.objects.get(pk=id)
            form = BudgetForm(instance=budget)
        return render(request, "pages/finance/budget_form.html", {'form': form})
    else:
        if id == 0:
            form = BudgetForm(request.POST)
        else:
            budget = BudgetMaster.objects.get(pk=id)
            form = BudgetForm(request.POST,instance= budget)
        if form.is_valid():
            form = form.save(commit=False)
            form.fin_year = "2020-2029"
            form.treasury_code = "01"
            form.issued_by = "abcd"
            form.user_code = "bc01"
            form.id = 1+int(get_random_string(8,'0123456789'))


            # a=form.fin_year = "2020-2029"
            # a=form.fin_year
            # form.treasury_code = "01"
            # form.issued_by = "abcd"
            # form.user_code = "bc01"
            # form.id = a.replace("-","")+form.treasury_code+form.issued_by+form.user_code

            form.save()
        return redirect('finance_budgetlist')

def budget_delete(request,id):
    budget = BudgetMaster.objects.get(pk=id)
    budget.delete()
    return redirect('finance_budgetlist')
