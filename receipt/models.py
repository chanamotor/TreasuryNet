from django.db import models

#TreasuryNET Models (4 Tables)
class ReceiptMaster(models.Model):
    #fin_year+treasury_code+tran_id
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    tran_id = models.IntegerField()
    major_head = models.CharField(max_length=4)
    scheme_code = models.CharField(max_length=13)
    ddo_code = models.CharField(max_length=7, blank=True)
    party_name = models.TextField()
    amount = models.BigIntegerField()
    entry_date = models.DateField()
    user_code = models.CharField(max_length=4)
    flag = models.CharField(max_length=2)
    online_tran_id = models.IntegerField(blank=True)
    
class FinalReceiptMaster(models.Model):
    #fin_year+treasury_code+tran_id
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    tran_id = models.IntegerField()
    major_head = models.CharField(max_length=4)
    scheme_code = models.CharField(max_length=13)
    ddo_code = models.CharField(max_length=7, blank=True)
    party_name = models.TextField()
    amount = models.BigIntegerField()
    entry_date = models.DateField()
    user_code = models.CharField(max_length=4)
    flag = models.CharField(max_length=2)
    online_tran_id = models.IntegerField(blank=True)
    voucher_no = models.IntegerField()
    payment_date = models.DateField()

class ReceiptVoucherSeq(models.Model):
    #fin_year+treasury_code+month+major_head+voucher_no
    id = models.CharField(max_length=21, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    major_head = models.CharField(max_length=4)
    voucher_no = models.IntegerField()

class ReceiptSeq(models.Model):
    #fin_year+treasury_code+online_tran_id
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    tran_id = models.IntegerField()
