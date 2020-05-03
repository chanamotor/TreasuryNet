from django.db import models

# 2 Tables.
class OnlineReceiptMaster(models.Model):
    #fin_year+treasury_code+online_tran_id
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_tran_id = models.IntegerField()
    major_head = models.CharField(max_length=4)
    scheme_code = models.CharField(max_length=13)
    ddo_code = models.CharField(max_length=7, blank=True)
    party_name = models.TextField()
    amount = models.BigIntegerField()
    date = models.DateField()

class OnlineReceiptSeq(models.Model):
    #fin_year+treasury_code+online_tran_id
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_tran_id = models.IntegerField()