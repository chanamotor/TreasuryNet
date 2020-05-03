from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth import (
    logout,
    authenticate,
    login as auth_login,
    update_session_auth_hash,
)
from .models import (
    OnlineBillMaster,
    OnlineBillDeductions,
    OnlineBillSubDetails,
    OnlineGpfTotal,
    OnlineGpfDetails,
    OnlineBillSeq,
)
from .forms import (
    OnlineBillMasterForm,
)

class IndexView(View):
    index_template = 'registration/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.index_template)

class DashboardView(View):
    tempalte_name = 'pages/department/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.tempalte_name)

class BillEntryView(View):
    tempalte_name = 'pages/department/bill_entry.html'
    form_class = OnlineBillMasterForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.tempalte_name, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            fin_year = '2020-2019'
            treasury_code = '10'
            try:
                onlineBillSeq = OnlineBillSeq.objects.filter(fin_year=fin_year,treasury_code=treasury_code).latest('online_bill_no')
            except OnlineBillSeq.DoesNotExist:
                onlineBillSeq = False
            
            if onlineBillSeq:
                online_bill_no = onlineBillSeq.online_bill_no
                online_bill_no+=1
            else:
                online_bill_no = 1

            master_id = fin_year+treasury_code+str(online_bill_no)

            context = {
                'form': form
            }

            if form.is_valid():
                form = form.save(commit=False)
                form.master_id = master_id
                form.treasury_code = treasury_code
                form.online_bill_no = online_bill_no
                form.save()

                OnlineBillSeq(
                    seq_id=master_id,
                    fin_year=fin_year,
                    treasury_code=treasury_code,
                    online_bill_no=online_bill_no
                ).save()
            else:
                context['error']: form.errors
            
            return render(request, self.tempalte_name, context)

class ViewBillView(View):
    tempalte_name = 'pages/department/view_bill.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.tempalte_name)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return render(request, self.tempalte_name)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/accounts/login/')
