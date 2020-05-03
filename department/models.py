from django.db import models

#TreasuryNET Models (8 Tables)
class OnlineBillMaster(models.Model):
    #fin_year+treasury_code+online_bill_no
    master_id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2, blank=True, null=True) # blank = True and null=True for testing 
    online_bill_no = models.IntegerField(blank=True)
    demand_no = models.CharField(max_length=2, blank=True, null=True) # blank = True and null=True for testing 
    ddo_code = models.CharField(max_length=7)
    detail_head = models.CharField(max_length=2)
    major_head = models.CharField(max_length=4, blank=True, null=True) # blank = True and null=True for testing 
    scheme_code = models.CharField(max_length=17)
    dept_bill_no = models.IntegerField()
    bill_type = models.CharField(max_length=2)
    date = models.DateField()
    net_amt = models.BigIntegerField()
    gross_amt = models.BigIntegerField(blank=True, null=True) # blank = True and null=True for testing
    status_flag = models.CharField(max_length=2, blank=True, null=True) # blank = True and null=True for testing

class OnlineBillDeductions(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'online_bill_no', 'scheme_code'),)
    #fin_year+treasury_code+onlinebill_no
    master_id = models.ForeignKey(OnlineBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_bill_no = models.IntegerField()
    scheme_code = models.CharField(max_length=17, blank=True)
    major_head = models.CharField(max_length=4, blank=True)
    amount = models.BigIntegerField(blank=True)
    deduction_flag = models.CharField(max_length=2, blank=True)

class OnlineBillSubDetails(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'online_bill_no', 'subdetail_head'),)
    #fin_year+treasury_code+onlinebill_no
    master_id = models.ForeignKey(OnlineBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_bill_no = models.IntegerField()
    subdetail_head = models.CharField(max_length=2, blank=True)
    amount = models.BigIntegerField(blank=True)

class OnlineGpfTotal(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'online_bill_no'),)
    #fin_year+treasury_code+onlinebill_no
    master_id = models.ForeignKey(OnlineBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_bill_no = models.IntegerField()
    sanction_no = models.TextField(blank=True)
    amount = models.BigIntegerField(blank=True)
    grade = models.IntegerField(blank=True)

class OnlineGpfDetails(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'online_bill_no', 'gpf_no'),)
    #fin_year+treasury_code+onlinebill_no
    master_id = models.ForeignKey(OnlineBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_bill_no = models.IntegerField()
    gpf_no = models.CharField(max_length=20, blank=True)
    subscriber_name = models.CharField(max_length=50, blank=True)
    amount = models.BigIntegerField(blank=True)

class OnlineBillSeq(models.Model):
    #fin_year+treasury_code+online_bill_no
    seq_id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    online_bill_no = models.IntegerField()

class DepartmentUsers(models.Model):
    user_name = models.CharField(max_length=30, primary_key=True)
    password = models.TextField()
    user_type = models.CharField(max_length=30)
    demand_no = models.CharField(max_length=2)

class EmployeeBankDetails(models.Model):
    class Meta:
        unique_together = (('account_no', 'ifsc', 'department_user'),)
    account_no = models.CharField(max_length=30)
    beneficiary_name = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    department_user = models.ForeignKey(DepartmentUsers, on_delete=models.CASCADE, null=True)