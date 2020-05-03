from django.contrib import admin

# Register your 4 models here.
from .models import (
    ReceiptMaster,
    FinalReceiptMaster,
    ReceiptVoucherSeq,
    ReceiptSeq
)
admin.site.register(ReceiptMaster)
admin.site.register(FinalReceiptMaster)
admin.site.register(ReceiptVoucherSeq)
admin.site.register(ReceiptSeq)