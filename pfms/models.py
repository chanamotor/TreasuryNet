from django.db import models

#TreasuryNET Models (3 Tables)
class PfmsFileSeq(models.Model):
    #fin_year+file_no
    id = models.CharField(max_length=15, primary_key=True)
    fin_year = models.CharField(max_length=9)
    file_no = models.IntegerField()

class PfmsSchemeMaster(models.Model):
    class Meta:
        unique_together = (('goi_code', 'budget_code'),)
    goi_code = models.CharField(max_length=5)
    budget_code = models.CharField(max_length=18)
    demand_no = models.CharField(max_length=2)
    detail_head = models.CharField(max_length=2)
    status = models.CharField(max_length=1)

class PfmsExpenditure(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no'),)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    budget_code = models.CharField(max_length=18)
    gross_amt = models.BigIntegerField()
    net_amt = models.BigIntegerField()
    accounting_date = models.DateField()
    filename = models.CharField(max_length=30)
    dated = models.DateField()