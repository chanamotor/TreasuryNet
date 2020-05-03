from django.db import models

#TreasuryNET Models (17 Tables)
class BillMaster(models.Model):
    #fin_year+treasury_code+bill_no
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    demand_no = models.CharField(max_length=2, blank=True)
    ddo_code = models.CharField(max_length=7)
    detail_head = models.CharField(max_length=2)
    major_head = models.CharField(max_length=4, blank=True)
    scheme_code = models.CharField(max_length=17)
    dept_bill_no = models.IntegerField()
    bill_type = models.CharField(max_length=2)
    entry_date = models.DateField()
    net_amt = models.BigIntegerField()
    gross_amt = models.BigIntegerField(blank=True)
    payment_type = models.CharField(max_length=2, blank=True)
    flag = models.CharField(max_length=2)
    online_bill_no = models.IntegerField(blank=True)

class FinalBillMaster(models.Model):
    #fin_year+treasury_code+bill_no
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    demand_no = models.CharField(max_length=2)
    ddo_code = models.CharField(max_length=7)
    detail_head = models.CharField(max_length=2)
    major_head = models.CharField(max_length=4)
    scheme_code = models.CharField(max_length=17)
    dept_bill_no = models.IntegerField()
    bill_type = models.CharField(max_length=2)
    entry_date = models.DateField()
    net_amt = models.BigIntegerField()
    gross_amt = models.BigIntegerField()
    payment_type = models.CharField(max_length=2)
    flag = models.CharField(max_length=2)
    online_bill_no = models.IntegerField(blank=True)
    voucher_no = models.IntegerField()
    accounting_date = models.DateField()
    encash_date = models.DateField()

class BillTrack(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no'),)
    #fin_year+treasury_code+bill_no
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    auditor_code = models.CharField(max_length=4, blank=True)
    audit_date = models.DateField()
    accountant_code = models.CharField(max_length=4, blank=True)
    acc_approved_date = models.DateField()
    authorizer_code = models.CharField(max_length=4, blank=True)
    authorized_date = models.DateField()
    flag = models.CharField(max_length=2)

class FinalBillTrack(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no'),)
    #fin_year+treasury_code+bill_no
    final_bill_master = models.ForeignKey(FinalBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    auditor_code = models.CharField(max_length=4, blank=True)
    audit_date = models.DateField()
    accountant_code = models.CharField(max_length=4, blank=True)
    acc_approved_date = models.DateField()
    authorizer_code = models.CharField(max_length=4, blank=True)
    authorized_date = models.DateField()
    flag = models.CharField(max_length=2)

class BillDeductions(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no', 'scheme_code'),)
    #fin_year+treasury_code+bill_no
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    scheme_code = models.CharField(max_length=13, blank=True)
    major_head = models.CharField(max_length=4, blank=True)
    amount = models.BigIntegerField(blank=True)
    flag = models.CharField(max_length=2, blank=True)
    voucher_no = models.IntegerField(blank=True)

class FinalBillDeductions(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no', 'scheme_code'),)
    #fin_year+treasury_code+bill_no
    final_bill_master = models.ForeignKey(FinalBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    scheme_code = models.CharField(max_length=13, blank=True)
    major_head = models.CharField(max_length=4, blank=True)
    amount = models.BigIntegerField(blank=True)
    flag = models.CharField(max_length=2, blank=True)
    voucher_no = models.IntegerField(blank=True)

class BillSubDetails(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no', 'subdetail_head'),)
    #fin_year+treasury_code+bill_no
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    subdetail_head = models.CharField(max_length=2, blank=True)
    amount = models.BigIntegerField(blank=True)

class FinalBillSubDetails(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no', 'subdetail_head'),)
    #fin_year+treasury_code+bill_no
    final_bill_master = models.ForeignKey(FinalBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    subdetail_head = models.CharField(max_length=2, blank=True)
    amount = models.BigIntegerField(blank=True)

class GpfTotal(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no'),)
    #fin_year+treasury_code+bill_no
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    sanction_no = models.TextField(blank=True)
    amount = models.BigIntegerField(blank=True)
    grade = models.IntegerField(blank=True)

class FinalGpfTotal(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no'),)
    #fin_year+treasury_code+bill_no
    final_bill_master = models.ForeignKey(FinalBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    sanction_no = models.TextField(blank=True)
    amount = models.BigIntegerField(blank=True)
    grade = models.IntegerField(blank=True)

class GpfDetails(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no', 'gpf_no'),)
    #fin_year+treasury_code+bill_no
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    gpf_no = models.CharField(max_length=20, blank=True)
    subscriber_name = models.CharField(max_length=50, blank=True)
    amount = models.BigIntegerField(blank=True)

class FinalGpfDetails(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no', 'gpf_no'),)
    #fin_year+treasury_code+bill_no
    final_bill_master = models.ForeignKey(FinalBillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    gpf_no = models.CharField(max_length=20, blank=True)
    subscriber_name = models.CharField(max_length=50, blank=True)
    amount = models.BigIntegerField(blank=True)

class AdviceRegister(models.Model):
    class Meta:
        unique_together = (('fin_year', 'treasury_code', 'bill_no'),)
    #fin_year+treasury_code+bill_no
    bill_master = models.ForeignKey(BillMaster, on_delete=models.CASCADE, null=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()
    advice_no = models.IntegerField()

class BudgetMaster(models.Model):
    #fin_year+treasury_code+ddo_code+detail_head+scheme_code+issue_date
    # class Meta:
    #     unique_together = (('fin_year', 'treasury_code', 'ddo_code','detail_head','scheme_code','issue_date'),)
    id = models.CharField(max_length=45, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    ddo_code = models.CharField(max_length=7)
    detail_head = models.CharField(max_length=2)
    scheme_code = models.CharField(max_length=17)
    issue_date = models.DateField()
    amount = models.BigIntegerField()
    order_no = models.TextField()
    da_no = models.IntegerField()
    valid_from = models.DateField()
    valid_to = models.DateField()
    issued_by = models.TextField(blank=True)
    user_code = models.CharField(max_length=4)

class PaymentVoucherSeq(models.Model):
    #fin_year+treasury_code+month+major_head+voucher_no
    id = models.CharField(max_length=21, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    major_head = models.CharField(max_length=4)
    voucher_no = models.IntegerField()

class BillSeq(models.Model):
    #fin_year+treasury_code+bill_no
    id = models.CharField(max_length=17, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    bill_no = models.IntegerField()

class AdviceSeq(models.Model):
    #fin_year+treasury_code+advice_date+advice_no
    id = models.CharField(max_length=25, primary_key=True)
    fin_year = models.CharField(max_length=9)
    treasury_code = models.CharField(max_length=2)
    advice_date = models.DateField()
    advice_no = models.IntegerField()
