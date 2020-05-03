from django import forms
from payment.models import BudgetMaster
from crispy_forms.helper import FormHelper

class BudgetForm(forms.ModelForm):

    DATEPICKER = {
            'type': 'text',
            'class': 'form-control',
            'id': 'kt_datepicker_1',
            'placeholder': 'Select date'
        }

    issue_date = forms.DateField(widget=forms.DateInput(attrs=DATEPICKER,format='%Y-%m-%d', ))
    valid_from = forms.DateField(widget=forms.DateInput(attrs=DATEPICKER,format='%Y-%m-%d', ))
    valid_to = forms.DateField(widget=forms.DateInput(attrs=DATEPICKER,format='%Y-%m-%d', ))
    


    class Meta:
        model = BudgetMaster
        #fields = ('ddo_code','detail_head','scheme_code','issue_date','order_no','da_no','valid_from','valid_to','amount')
        exclude = ['id','fin_year','treasury_code','issued_by','user_code']

        labels = {
            'ddo_code':'DDO Code',
            'detail_head':'Detail Head'
        }

    def __init__(self, *args, **kwargs):
        super(BudgetForm,self).__init__(*args, **kwargs)
        self.fields['ddo_code'].empty_label = "Select"
        self.fields['detail_head'].empty_label = "Select"
        self.fields['scheme_code'].empty_label = "Select"
        self.helper = FormHelper()
        self.helper.form_show_labels = False
