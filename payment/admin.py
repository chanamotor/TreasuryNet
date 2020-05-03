from django.contrib import admin

# Register your models 12 here.
# Register your models 12 here.
from .models import (
    BillMaster,
    FinalBillMaster,
    BillTrack,
    FinalBillTrack,
    BillDeductions,
    FinalBillDeductions,
    BillSubDetails,
    FinalBillSubDetails,
    GpfTotal,
    FinalGpfTotal,
    GpfDetails,
    FinalGpfDetails,
    AdviceRegister,
    BudgetMaster,
    BillSeq,
    AdviceSeq,
    PaymentVoucherSeq
)
admin.site.register(BillMaster)
admin.site.register(FinalBillMaster)
admin.site.register(BillTrack)
admin.site.register(FinalBillTrack)
admin.site.register(BillDeductions)
admin.site.register(FinalBillDeductions)
admin.site.register(BillSubDetails)
admin.site.register(FinalBillSubDetails)
admin.site.register(GpfTotal)
admin.site.register(FinalGpfTotal)
admin.site.register(GpfDetails)
admin.site.register(FinalGpfDetails)
admin.site.register(AdviceRegister)
admin.site.register(BudgetMaster)
admin.site.register(BillSeq)
admin.site.register(AdviceSeq)
admin.site.register(PaymentVoucherSeq)
