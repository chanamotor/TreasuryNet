from django.db import models

#TreasuryNET Models (18 Tables)
class Treasury(models.Model):
    treasury_code = models.CharField(max_length=2, primary_key=True)
    treasury_name = models.TextField()
    address = models.TextField(blank=True)
    treasury_type = models.CharField(max_length=12)

class Department(models.Model):
    demand_no = models.CharField(max_length=2, primary_key=True)
    dept_name = models.TextField()

class Ddo(models.Model):
    ddo_code = models.CharField(max_length=7, primary_key=True)
    ddo_name = models.TextField()

class DetailHead(models.Model):
    detail_head = models.CharField(max_length=2, primary_key=True)
    description = models.TextField()

class Classification(models.Model):
    classification_code = models.CharField(max_length=2, primary_key=True)
    classification_name = models.TextField()

class PaymentSchemes(models.Model):
    scheme_code = models.CharField(max_length=17, primary_key=True)
    scheme_name = models.TextField()

class SubDetailHeads(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    detail_head = models.CharField(max_length=2)
    subdetail_head = models.CharField(max_length=2)
    description = models.TextField()
    detail_head_ref = models.ForeignKey(DetailHead, on_delete=models.CASCADE, null=True)

class BillType(models.Model):
    bill_type = models.CharField(max_length=2, primary_key=True)
    description = models.TextField()                                                                                                                                                                                                                                                      

class DdoSchemeMap(models.Model):
    #treasury_code+ddo_code+scheme_code
    id = models.CharField(max_length=26, primary_key=True)
    treasury_code = models.CharField(max_length=2)
    ddo_code = models.ForeignKey(Ddo, on_delete=models.CASCADE, null=True)
    scheme_code = models.ForeignKey(PaymentSchemes, on_delete=models.CASCADE, null=True)

class Operators(models.Model):
    #treasury_code+user_code
    id = models.CharField(max_length=6, primary_key=True)
    treasury_code = models.CharField(max_length=2)
    operator_code = models.CharField(max_length=4)
    operator_type = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=50)
    password = models.TextField()
    designation = models.CharField(max_length=50)

class OperatorDdoMap(models.Model):
    class Meta:
        unique_together = (('operator', 'ddo_code'),)
    operator = models.ForeignKey(Operators, on_delete=models.CASCADE, null=True)
    ddo_code = models.CharField(max_length=7)
    operator_type = models.CharField(max_length=50)

class MajorHead(models.Model):
	id = models.CharField(max_length=6, primary_key=True)
	demand_no = models.CharField(max_length=2)
	major_head = models.CharField(max_length=4)
	major_head_name = models.TextField()

class SubMajorHead(models.Model):
	id = models.CharField(max_length=8, primary_key=True)
	demand_no = models.CharField(max_length=2)
	major_head = models.CharField(max_length=4)
	submajor_head = models.CharField(max_length=2)
	submajor_head_name = models.TextField()
	major_head_ref = models.ForeignKey(MajorHead, on_delete=models.CASCADE, null=True)

class MinorHead(models.Model):
	id = models.CharField(max_length=11, primary_key=True)
	demand_no = models.CharField(max_length=2)
	major_head = models.CharField(max_length=4)
	submajor_head = models.CharField(max_length=2)
	minor_head = models.CharField(max_length=3)
	minor_head_name = models.TextField()
	submajor_head_ref = models.ForeignKey(SubMajorHead, on_delete=models.CASCADE, null=True)

class SchemeHead(models.Model):
	id = models.CharField(max_length=13, primary_key=True)
	demand_no = models.CharField(max_length=2)
	major_head = models.CharField(max_length=4)
	submajor_head = models.CharField(max_length=2)
	minor_head = models.CharField(max_length=3)
	scheme_head = models.CharField(max_length=2)
	scheme_head_name = models.TextField()
	minor_head_ref = models.ForeignKey(MinorHead, on_delete=models.CASCADE, null=True)

class SubSchemeHead(models.Model):
	id = models.CharField(max_length=15, primary_key=True)
	demand_no = models.CharField(max_length=2)
	major_head = models.CharField(max_length=4)
	submajor_head = models.CharField(max_length=2)
	minor_head = models.CharField(max_length=3)
	scheme_head = models.CharField(max_length=2)
	subscheme_head = models.CharField(max_length=2)
	subscheme_head_name = models.TextField()
	scheme_head_ref = models.ForeignKey(SchemeHead, on_delete=models.CASCADE, null=True)

class ReceiptSchemes(models.Model):
    scheme_code = models.CharField(max_length=13, primary_key=True)
    scheme_name = models.TextField()

class DeductionSchemes(models.Model):
    scheme_code = models.CharField(max_length=13, primary_key=True)
    flag = models.CharField(max_length=1)
    receipt_scheme_ref = models.ForeignKey(ReceiptSchemes, on_delete=models.CASCADE, null=True)