from django.db import models
from payment.models import BillMaster, FinalBillMaster

#TreasuryNET Models (7 Tables)
class CmpUploadSeq(models.Model):
    #fin_year+treasury_code+file_upload_no
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    file_upload_no = models.IntegerField()

class CmpTransactionSeq(models.Model):
    #fin_year+treasury_code+transaction_no
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    transaction_no = models.IntegerField()

class CmpBillMaster(models.Model):
    #fin_year+treasury_code+bill_no
    id = models.CharField(max_length=17, primary_key=True)
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    ddo_code = models.CharField(max_length=7)
    scheme_code = models.CharField(max_length=17)
    dept_bill_no = models.IntegerField()
    detail_head = models.CharField(max_length=2)
    bill_type = models.CharField(max_length=2)
    detail_desc = models.CharField(max_length=50)
    net_amt = models.BigIntegerField()
    payment_date = models.DateField()
    payment_ref_no = models.TextField()
    bill_identifier = models.CharField(max_length=1)
    file_upload_no = models.IntegerField()
    transaction_id = models.IntegerField()
    transaction_date = models.DateField()

class FinalCmpBillMaster(models.Model):
    #fin_year+treasury_code+bill_no
    id = models.CharField(max_length=17, primary_key=True)
    bill_master = models.ForeignKey(FinalBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    ddo_code = models.CharField(max_length=7)
    scheme_code = models.CharField(max_length=17)
    dept_bill_no = models.IntegerField()
    detail_head = models.CharField(max_length=2)
    bill_type = models.CharField(max_length=2)
    detail_desc = models.CharField(max_length=50)
    net_amt = models.BigIntegerField()
    payment_date = models.DateField()
    payment_ref_no = models.TextField()
    bill_identifier = models.CharField(max_length=1)
    file_upload_no = models.IntegerField()
    transaction_id = models.IntegerField()
    transaction_date = models.DateField()

class CmpTemp(models.Model):
    #fin_year+treasury_code+bill_no+account_no
    id = models.CharField(max_length=40, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    account_no = models.CharField(max_length=30)
    beneficiary_name = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    file_upload_no = models.IntegerField()
    amount = models.BigIntegerField()

class CmpEmployeeDetails(models.Model):
    #fin_year+treasury_code+bill_no+account_no
    id = models.CharField(max_length=40, primary_key=True)
    cmp_bill_master = models.ForeignKey(CmpBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    account_no = models.CharField(max_length=30)
    beneficiary_name = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    file_upload_no = models.IntegerField()
    amount = models.BigIntegerField()

class FinalCmpEmployeeDetails(models.Model):
    #fin_year+treasury_code+bill_no+account_no
    id = models.CharField(max_length=40, primary_key=True)
    final_cmp_bill_master = models.ForeignKey(FinalCmpBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    account_no = models.CharField(max_length=30)
    beneficiary_name = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    file_upload_no = models.IntegerField()
    amount = models.BigIntegerField()