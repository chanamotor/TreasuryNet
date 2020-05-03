from django import forms
from .models import (
    OnlineBillMaster,
    OnlineBillDeductions,
    OnlineBillSubDetails,
    OnlineGpfTotal,
    OnlineGpfDetails,
    OnlineBillSeq,
)

class OnlineBillMasterForm(forms.ModelForm):

    master_id = forms.CharField(max_length=17, required=False) #test
    fin_year = forms.CharField(max_length=9)
    treasury_code = forms.CharField(max_length=2, required=False) #test
    online_bill_no = forms.IntegerField(required=False) #test
    demand_no = forms.CharField(max_length=2, required=False) #test
    ddo_code = forms.CharField(max_length=7)
    detail_head = forms.CharField(max_length=2)
    major_head = forms.CharField(max_length=4, required=False) 
    scheme_code = forms.CharField(max_length=17)
    dept_bill_no = forms.IntegerField()
    bill_type = forms.CharField(max_length=2)
    date = forms.DateField()
    net_amt = forms.IntegerField()
    gross_amt = forms.IntegerField(required=False)
    status_flag = forms.CharField(max_length=2, required=False)

    class Meta:
        model = OnlineBillMaster
        fields = "__all__"
        # fields = ( 
        #     "master_id",
        #     "fin_year",
        #     "treasury_code",
        #     "online_bill_no",
        #     "demand_no",
        #     "ddo_code",
        #     "detail_head",
        #     "major_head",
        #     "scheme_code",
        #     "dept_bill_no",
        #     "bill_type",
        #     "date",
        #     "net_amt",
        #     "gross_amt",
        #     "status_flag"
        # )

# class OnlineBillSeqForm(forms.ModelForm):
#     #fin_year+treasury_code+online_bill_no
#     seq_id = models.CharField(max_length=17, primary_key=True)
#     fin_year = models.CharField(max_length=9)
#     treasury_code = models.CharField(max_length=2)
#     online_bill_no = models.IntegerField()