from django.contrib import admin

# Register your 4 models here.
from .models import (
    CmpUploadSeq,
    CmpTransactionSeq,
    CmpBillMaster,
    FinalCmpBillMaster,
    CmpEmployeeDetails,
    FinalCmpEmployeeDetails
)
admin.site.register(CmpUploadSeq)
admin.site.register(CmpTransactionSeq)
admin.site.register(CmpBillMaster)
admin.site.register(FinalCmpBillMaster)
admin.site.register(CmpEmployeeDetails)
admin.site.register(FinalCmpEmployeeDetails)